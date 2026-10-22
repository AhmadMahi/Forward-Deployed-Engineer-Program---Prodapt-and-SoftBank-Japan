"""SmartDesk LLM client.

Online when OPENAI_API_KEY is set. Offline demo mode when there is no key or OFFLINE=1,
so every test and demo runs without a key. Offline output shows how the code works, not real model quality.
"""
import json
import os
import re

# Default model: confirm against the approved model list (docs/MODEL_GUIDE.md). Override with LLM_MODEL.
MODEL = os.getenv("LLM_MODEL", "gpt-6.1-sol")


def is_online():
    return os.getenv("OFFLINE") != "1" and bool(os.getenv("OPENAI_API_KEY"))


_ENC = []


def count_tokens(text):
    if not _ENC:
        try:
            import tiktoken
            _ENC.append(tiktoken.get_encoding("o200k_base"))
        except Exception:
            _ENC.append(None)                    # no tiktoken or no download: use the estimate
    if _ENC[0] is not None:
        return len(_ENC[0].encode(text))
    return max(1, round(len(text) / 4))          # about 4 characters per token


def offline_reply(prompt, system=""):
    """A deliberately simple stand-in. It is not intelligent; it lets the code paths run."""
    first = re.split(r"(?<=[.!?])\s+", prompt.strip().splitlines()[-1].strip())[0]
    return f"[offline demo] {first[:160]}"


def complete(prompt, system="You are a SmartDesk support assistant.", max_tokens=300, json_schema=None,
             model=None):
    """Return (text, usage). usage has input_tokens and output_tokens."""
    if is_online():
        from openai import OpenAI
        client = OpenAI(timeout=20, max_retries=1)      # reads OPENAI_API_KEY from the environment
        kwargs = {}
        if json_schema:
            kwargs["response_format"] = {"type": "json_schema",
                                         "json_schema": {"name": "output", "schema": json_schema, "strict": True}}
        r = client.chat.completions.create(
            model=model or MODEL, max_completion_tokens=max_tokens,
            messages=[{"role": "system", "content": system}, {"role": "user", "content": prompt}], **kwargs)
        return r.choices[0].message.content, {"input_tokens": r.usage.prompt_tokens,
                                              "output_tokens": r.usage.completion_tokens}
    text = offline_reply(prompt, system)
    if json_schema:
        text = json.dumps({"offline": True, "text": text})
    return text, {"input_tokens": count_tokens(system + prompt), "output_tokens": count_tokens(text)}
