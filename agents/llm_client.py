import os
import time
import json
import functools
import logging
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

logger = logging.getLogger('sylon.llm')
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('[%(asctime)s] [%(name)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    logger.addHandler(handler)

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

DASHSCOPE_API_KEY = os.environ.get("DASHSCOPE_API_KEY", "")

qwen_client = None
if DASHSCOPE_API_KEY and OpenAI:
    base_url = os.environ.get("QWEN_BASE_URL", "https://dashscope-intl.aliyuncs.com/compatible-mode/v1")
    qwen_client = OpenAI(
        api_key=DASHSCOPE_API_KEY,
        base_url=base_url,
    )

QWEN_FAST_MODEL = os.environ.get("QWEN_FAST_MODEL", "qwen-plus")
QWEN_REASONING_MODEL = os.environ.get("QWEN_REASONING_MODEL", "qwen-max")

logger.info(f"[INIT] Primary fast engine: {QWEN_FAST_MODEL} | Reasoning engine: {QWEN_REASONING_MODEL}")

MAX_RETRIES = 3
BASE_DELAY = 2

def retry_with_backoff(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        delay = BASE_DELAY
        for attempt in range(MAX_RETRIES):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                err_msg = str(e).lower()
                if "429" in err_msg or "rate limit" in err_msg or "quota" in err_msg:
                    if attempt == MAX_RETRIES - 1:
                        logger.error(f"[LLM Rate Limit] Failed after {MAX_RETRIES} attempts.")
                        raise e
                    logger.warning(f"[LLM Rate Limit] Retrying in {delay}s... (Attempt {attempt+1}/{MAX_RETRIES})")
                    time.sleep(delay)
                    delay *= 2
                else:
                    raise e
    return wrapper


@retry_with_backoff
def call_llm(prompt: str, system_prompt: str = "You are a helpful assistant.", temperature: float = 0.7, max_tokens: int = 2000, model_override: str = None) -> str:
    """
    Standard generation call using Qwen Cloud via DashScope compatible API.
    """
    if not qwen_client:
        raise ValueError("Qwen Cloud API key is missing. Please set DASHSCOPE_API_KEY in your .env file.")

    try:
        target_model = model_override or QWEN_FAST_MODEL
        logger.info(f"[QWEN] Calling model: {target_model}")
        response = qwen_client.chat.completions.create(
            model=target_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"[QWEN] Call failed: {e}")
        raise e


@retry_with_backoff
def call_cerebras(prompt: str, system_prompt: str = None, model_override: str = None, **kwargs) -> str:
    # Keeping the function signature for compatibility, but routing to Qwen
    return call_llm(prompt, system_prompt=system_prompt or "You are a helpful assistant.", model_override=model_override, **kwargs)


@retry_with_backoff
def call_llm_json(prompt: str, system_prompt: str = "You are a helpful assistant.", temperature: float = 0.1, max_tokens: int = 4000, model_override: str = None) -> dict:
    """
    Calls Qwen in JSON mode.
    """
    if not qwen_client:
        raise ValueError("Qwen Cloud API key is missing. Please set DASHSCOPE_API_KEY in your .env file.")

    try:
        target_model = model_override or QWEN_FAST_MODEL
        logger.info(f"[QWEN JSON] Calling model: {target_model}")
        response = qwen_client.chat.completions.create(
            model=target_model,
            messages=[
                {"role": "system", "content": system_prompt + "\nIMPORTANT: You must output ONLY valid JSON. Do not include markdown code blocks or any other text."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            response_format={"type": "json_object"}
        )
        content = response.choices[0].message.content
        return json.loads(content)
    except Exception as e:
        logger.error(f"[QWEN JSON] Call failed: {e}")
        # Try to clean markdown if parsing failed
        try:
            if "content" in locals():
                import re
                match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', content)
                if match:
                    return json.loads(match.group(1))
                cleaned = content.strip()
                return json.loads(cleaned)
        except Exception:
            pass
        raise e


@retry_with_backoff
def call_cerebras_json(prompt: str, system_prompt: str = None, temperature: float = 0.1, max_tokens: int = 4000, model_override: str = None) -> dict:
    # Kept for compatibility, routes to Qwen JSON mode
    return call_llm_json(prompt, system_prompt=system_prompt or "You are a helpful assistant.", temperature=temperature, max_tokens=max_tokens, model_override=model_override)


@retry_with_backoff
def call_gemini_structured(prompt: str, response_schema=None) -> str:
    if os.environ.get("SYLON_DEBUG_MODE") == "True":
        return "CHAT"

    # Previously used Gemini, now routes to Qwen JSON and stringifies
    result_dict = call_llm_json(prompt)
    return json.dumps(result_dict)
