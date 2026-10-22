"""SmartDesk step 28: a resilient LLM client. Retries with backoff, model fallback, circuit breaker, timeouts."""
import random
import time


class TransientError(Exception):
    """Rate limits, timeouts and 5xx errors: worth retrying."""


class CircuitOpen(Exception):
    pass


class CircuitBreaker:
    def __init__(self, failures=3, reset_after=30.0, clock=time.monotonic):
        self.limit, self.reset_after, self.clock = failures, reset_after, clock
        self.count, self.opened_at = 0, None

    def allow(self):
        if self.opened_at is None:
            return True
        if self.clock() - self.opened_at >= self.reset_after:
            self.opened_at, self.count = None, 0          # half-open: try again
            return True
        return False

    def record(self, ok):
        self.count = 0 if ok else self.count + 1
        if self.count >= self.limit:
            self.opened_at = self.clock()


class ResilientClient:
    def __init__(self, providers, retries=2, base_delay=0.2, sleep=time.sleep):
        """providers: list of (model_name, callable(prompt) -> (text, usage)), primary first."""
        self.providers = providers
        self.breakers = {name: CircuitBreaker() for name, _ in providers}
        self.retries, self.base_delay, self.sleep = retries, base_delay, sleep
        self.log = []

    def complete(self, prompt):
        for name, call in self.providers:
            if not self.breakers[name].allow():
                self.log.append((name, "skipped: circuit open"))
                continue
            for attempt in range(self.retries + 1):
                try:
                    text, usage = call(prompt)
                    self.breakers[name].record(True)
                    self.log.append((name, "ok"))
                    return {"model": name, "text": text, "usage": usage, "attempts": attempt + 1}
                except TransientError as e:
                    self.breakers[name].record(False)
                    self.log.append((name, f"retry {attempt + 1}: {e}"))
                    if attempt < self.retries:
                        self.sleep(self.base_delay * 2 ** attempt + random.uniform(0, 0.05))
        raise CircuitOpen("All providers failed. Show a friendly message and queue the ticket for a human.")
