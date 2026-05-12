"""
Centralized LLM Client for Sylon.

Two providers, one interface:
- Cerebras AI (Llama 3.3 70B) → heavy lifting (collision, strategist, painpoints, parsing)
- Gemini → Router structured output only

All retry logic lives here — no more copy-pasting across agents.
"""
import os
import time
import json
import functools
# pyrefly: ignore [missing-import]
from google import genai
# pyrefly: ignore [missing-import]
from openai import OpenAI
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# ---------------------------------------------------------------------------
# Clients
# ---------------------------------------------------------------------------
gemini_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

cerebras_client = OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key=os.environ.get("CEREBRAS_API_KEY", "placeholder"),
)

CEREBRAS_MODEL = os.environ.get("CEREBRAS_MODEL", "llama-3.3-70b")
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

# ---------------------------------------------------------------------------
# Retry logic (shared)
# ---------------------------------------------------------------------------
MAX_RETRIES = 4
BASE_DELAY = 3  # seconds


def retry_with_backoff(func):
    """Decorator that retries on rate-limit (429 / ResourceExhausted) errors."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                err_msg = str(e).lower()
                is_rate_limit = (
                    "429" in err_msg
                    or ("resource" in err_msg and "exhausted" in err_msg)
                    or "rate" in err_msg
                )
                if is_rate_limit and attempt < MAX_RETRIES:
                    wait = BASE_DELAY * (2 ** (attempt - 1))
                    print(f"[LLM Retry] Rate-limited on {func.__name__}, attempt {attempt}/{MAX_RETRIES}. Waiting {wait}s...")
                    time.sleep(wait)
                else:
                    raise
    return wrapper


# ---------------------------------------------------------------------------
# Cerebras (primary — used for everything except Router)
# ---------------------------------------------------------------------------
@retry_with_backoff
def call_cerebras(
    prompt: str,
    system_prompt: str = "",
    temperature: float = 0.7,
    max_tokens: int = 2000,
) -> str:
    """
    Single function for all Cerebras calls.

    Args:
        prompt: User/content prompt.
        system_prompt: Optional system instruction.
        temperature: Sampling temperature.
        max_tokens: Max output tokens.

    Returns:
        The model's text response.
    """
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    response = cerebras_client.chat.completions.create(
        model=CEREBRAS_MODEL,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


@retry_with_backoff
def call_cerebras_json(
    prompt: str,
    system_prompt: str = "",
    temperature: float = 0.4,
    max_tokens: int = 4000,
) -> dict | list:
    """
    Cerebras call that forces JSON output and parses it.
    Falls back to extracting JSON from markdown fences if needed.
    """
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    response = cerebras_client.chat.completions.create(
        model=CEREBRAS_MODEL,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        response_format={"type": "json_object"},
    )
    raw = response.choices[0].message.content

    # Try direct parse
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    # Try extracting from markdown fences
    import re
    match = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", raw, re.DOTALL)
    if match:
        return json.loads(match.group(1))

    raise ValueError(f"Could not parse JSON from Cerebras response: {raw[:200]}")


# ---------------------------------------------------------------------------
# Gemini (Router only — structured enum output)
# ---------------------------------------------------------------------------
@retry_with_backoff
def call_gemini_structured(prompt: str, response_schema) -> str:
    """
    For Router enum classification. Uses Gemini's structured output.

    Args:
        prompt: The classification prompt.
        response_schema: An enum class for structured output.

    Returns:
        The enum value as a string.
    """
    response = gemini_client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "response_mime_type": "text/x.enum",
            "response_schema": response_schema,
        },
    )
    return response.text.strip()


@retry_with_backoff
def call_gemini(prompt: str, json_mode: bool = False) -> str:
    """
    General Gemini call (fallback if Cerebras is down).

    Args:
        prompt: The prompt text.
        json_mode: If True, request JSON output.

    Returns:
        The model's text response.
    """
    config = {}
    if json_mode:
        config["response_mime_type"] = "application/json"

    response = gemini_client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=config if config else None,
    )
    return response.text
