"""SmartDesk step 30: OpenTelemetry traces with GenAI semantic convention attributes, plus token and cost per trace."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

from token_cost import cost

EXPORTER = InMemorySpanExporter()             # swap for an OTLP exporter in production
_provider = TracerProvider()
_provider.add_span_processor(SimpleSpanProcessor(EXPORTER))
tracer = _provider.get_tracer("smartdesk")


def traced_llm_call(model, prompt, call):
    """Wrap any LLM call. call(prompt) -> (text, usage)."""
    with tracer.start_as_current_span(f"chat {model}") as span:
        span.set_attribute("gen_ai.operation.name", "chat")
        span.set_attribute("gen_ai.provider.name", "openai")
        span.set_attribute("gen_ai.request.model", model)
        text, usage = call(prompt)
        span.set_attribute("gen_ai.usage.input_tokens", usage["input_tokens"])
        span.set_attribute("gen_ai.usage.output_tokens", usage["output_tokens"])
        span.set_attribute("smartdesk.cost_estimate", cost(usage["input_tokens"], usage["output_tokens"]))
        return text


def per_trace_totals():
    totals = {}
    for s in EXPORTER.get_finished_spans():
        t = totals.setdefault(s.context.trace_id, {"tokens": 0, "cost": 0.0, "spans": 0})
        t["tokens"] += s.attributes.get("gen_ai.usage.input_tokens", 0) + s.attributes.get("gen_ai.usage.output_tokens", 0)
        t["cost"] += s.attributes.get("smartdesk.cost_estimate", 0.0)
        t["spans"] += 1
    return totals


def ticket_trace(ticket_text, call):
    """One user request = one trace with several LLM spans (classify, then answer)."""
    with tracer.start_as_current_span("smartdesk.handle_ticket"):
        label = traced_llm_call("small-classifier", f"Classify: {ticket_text}", call)
        return traced_llm_call("gpt-6.1-sol", f"Answer ({label}): {ticket_text}", call)
