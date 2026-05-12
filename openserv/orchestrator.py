import os
import sys
import yaml
import json
import time
# pyrefly: ignore [missing-import]
import enum
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.llm_client import call_cerebras, call_gemini_structured, retry_with_backoff
from agents.persona_factory import get_personas_for_business, generate_synthetic_personas
from agents.review_ingest import ingest_text, load_reviews, get_review_count
from agents.painpoint_extractor import load_painpoints, load_personas
from openserv.tools import (
    tool_run_collision_simulation,
    tool_generate_synthetic_personas,
    tool_fetch_competitor_personas,
    tool_ingest_reviews,
    tool_extract_painpoints,
)

load_dotenv()

# Load agents config
with open(os.path.join(os.path.dirname(__file__), 'agents.yaml'), 'r') as f:
    agents_config = yaml.safe_load(f)['agents']

# --- Structured Output Schema for Router ---
class Route(enum.Enum):
    SIMULATE = "SIMULATE"
    CHAT = "CHAT"
    INGEST = "INGEST"

# ---------------------------------------------------------------------------
# Session state: tracks the current business_id across the conversation
# In production this would be per-session; for the demo a global is fine.
# ---------------------------------------------------------------------------
_current_business_id = None


def set_business_id(business_id: str):
    global _current_business_id
    _current_business_id = business_id


def get_business_id() -> str | None:
    return _current_business_id


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------
@retry_with_backoff
def evaluate_route(user_input: str) -> str:
    """
    Uses the Router Agent to classify user intent.
    Returns 'SIMULATE', 'CHAT', or 'INGEST'.
    Defaults to 'CHAT' on any failure.
    """
    try:
        result = call_gemini_structured(
            prompt=f"{agents_config['router']['system_prompt']}\n\nUser input: \"{user_input}\"",
            response_schema=Route,
        )
        return result
    except Exception as e:
        err_msg = str(e).lower()
        is_rate_limit = "429" in err_msg or ("resource" in err_msg and "exhausted" in err_msg)
        if is_rate_limit:
            raise  # let the retry decorator handle it
        print(f"[Router Failsafe] Router failed ({type(e).__name__}), defaulting to CHAT.")
        return "CHAT"


# ---------------------------------------------------------------------------
# Strategist (Cerebras-powered)
# ---------------------------------------------------------------------------
@retry_with_backoff
def simulate_strategist(user_input: str, collision_result: str, painpoints: dict = None) -> str:
    """Formats the Simulator's raw output into conversational Strategist advice."""
    painpoint_context = ""
    if painpoints and painpoints.get("complaints"):
        top_complaints = [c["theme"] for c in painpoints["complaints"][:3]]
        painpoint_context = f"\n\nKNOWN CUSTOMER PAINPOINTS: {', '.join(top_complaints)}\nYour advice MUST address how the proposed change relates to these real issues."

    prompt = f"""{agents_config['strategist']['system_prompt']}

USER SCENARIO: "{user_input}"

SIMULATOR ANALYSIS (Multi-Persona):
{collision_result}
{painpoint_context}

You have received collision analyses from MULTIPLE distinct customer archetypes.
Synthesize these into a single, unified verdict for the business owner.
Highlight where the personas agree (strong signal) and where they disagree (nuance).
Keep it conversational. 3-5 punchy sentences.
If real customer quotes were cited in the analysis, reference them naturally."""

    return call_cerebras(
        prompt=prompt,
        system_prompt="You are Sylon, a premium business strategist. Be conversational, sharp, and authoritative.",
        temperature=0.7,
        max_tokens=800,
    )


@retry_with_backoff
def direct_chat_strategist(user_input: str) -> str:
    """Handles general conversation without running the Simulator."""
    business_id = get_business_id()
    context = ""
    if business_id:
        review_count = get_review_count(business_id)
        if review_count > 0:
            context = f"\n\nContext: You have {review_count} customer reviews loaded for this business."

    prompt = f"""{agents_config['strategist']['system_prompt']}

The business owner said: "{user_input}"
{context}
This is a general question or greeting—NOT a business scenario to simulate.
Respond conversationally as Sylon, a premium business strategist.
Briefly explain what you can do if they ask, or respond naturally to their greeting.
Keep it to 2-3 sentences max."""

    return call_cerebras(
        prompt=prompt,
        system_prompt="You are Sylon, a premium business strategist. Be conversational and sharp.",
        temperature=0.7,
        max_tokens=400,
    )


# ---------------------------------------------------------------------------
# INGEST handler (new)
# ---------------------------------------------------------------------------
def handle_ingest(user_input: str) -> str:
    """
    Handles review ingestion from pasted text.
    Generates a business_id if none exists, parses the reviews,
    extracts painpoints, and excavates grounded personas.
    """
    import uuid

    business_id = get_business_id()
    if not business_id:
        business_id = f"biz_{uuid.uuid4().hex[:8]}"
        set_business_id(business_id)
        print(f"[Ingest] Created new business_id: {business_id}")

    # Parse the pasted reviews
    print(f"[Ingest] Parsing pasted reviews for {business_id}...")
    reviews = tool_ingest_reviews(business_id=business_id, reviews_text=user_input)

    if not reviews:
        return "I couldn't find any reviews in what you shared. Try pasting the actual review text — even messy formatting works."

    # Extract painpoints and build personas
    print(f"[Ingest] Extracting painpoints and building personas...")
    result = tool_extract_painpoints(business_id=business_id)

    complaint_count = len(result.get("painpoints", {}).get("complaints", []))
    praise_count = len(result.get("painpoints", {}).get("praise", []))
    persona_count = len(result.get("personas", []))
    review_count = result.get("review_count", len(reviews))

    # Build a natural response
    persona_names = [p.get("name", "Unknown") for p in result.get("personas", [])]
    top_complaints = [c["theme"] for c in result.get("painpoints", {}).get("complaints", [])[:3]]

    response_parts = [f"Got it. I processed {review_count} reviews"]

    if complaint_count > 0:
        response_parts.append(f"and found {complaint_count} key pain points")
    if persona_count > 0:
        response_parts.append(f"I identified {persona_count} distinct customer types: {', '.join(persona_names)}")
    if top_complaints:
        response_parts.append(f"The biggest issues your customers mention: {', '.join(top_complaints)}")

    response_parts.append("Now ask me anything about your business — my advice will be grounded in what your real customers are saying.")

    return ". ".join(response_parts)


# ---------------------------------------------------------------------------
# Simulation Pipeline (updated for grounded personas)
# ---------------------------------------------------------------------------
def get_local_persona():
    """Legacy fallback: pre-excavated Yelp persona."""
    persona_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'outputs', 'bJ5FtCtZX3ZZacz2_2PJjA_persona.json')
    try:
        with open(persona_path, 'r') as f:
            raw_persona = json.load(f)
            persona_narrative = raw_persona.get('narrative', '')
            drifts = raw_persona.get('structured', {}).get('drifts', [])
            recent_signal = raw_persona.get('structured', {}).get('phases', {}).get('recent', {}).get('signal', {})
            recent_rating = recent_signal.get('avg_rating', 0)
            top_words = recent_signal.get('top_words', [])
    except FileNotFoundError:
        print("Warning: Pre-excavated persona not found. Using a mock persona.")
        persona_narrative = "This user loves quiet, cheap places and hates loud noises."
        drifts = []
        recent_rating = 3.0
        top_words = ["quiet", "cheap", "noise"]

    return persona_narrative, drifts, recent_rating, top_words


def run_simulation(user_input: str, business_description: str = "Local Cafe, Coffee Shop", location: str = "") -> str:
    """
    Multi-Persona Simulation Pipeline — now with grounded persona support.

    If a business_id is set and has reviews:
      → Uses grounded personas + painpoints from real reviews
    Otherwise:
      → Falls back to synthetic personas (Phase 1) + Google Places (Phase 2)
    """
    business_id = get_business_id()
    business_attributes = {
        'name': business_description.split(',')[0].strip(),
        'categories': business_description,
        'price_range': 'mid-range',
        'noise_level': 'average'
    }

    all_collisions = []
    painpoints = None

    # --- Try grounded personas first ---
    if business_id:
        personas, painpoints, mode = get_personas_for_business(
            business_id=business_id,
            business_description=business_description,
            location=location,
            persona_count=int(os.environ.get("SYLON_PERSONA_COUNT", "2")),
        )

        if personas:
            print(f"[Simulator] Using {len(personas)} personas in {mode} mode")
            simulator_rules = f"\n{agents_config['simulator']['system_prompt']}\nOwner's scenario: \"{user_input}\""

            for persona in personas:
                print(f"  [Simulator] Running collision for: {persona['name']} ({persona.get('source', 'unknown')})")
                try:
                    result = tool_run_collision_simulation(
                        persona_narrative=persona['narrative'] + "\n\nSIMULATOR RULES:" + simulator_rules,
                        persona_drifts=persona.get('drifts', []),
                        recent_rating=persona.get('avg_rating', 3.5),
                        top_words=persona.get('top_words', []),
                        business_attributes=business_attributes,
                        painpoints=painpoints,
                        grounding_quotes=persona.get('grounding_quotes', []),
                    )
                    source_tag = f" ({persona.get('source', '')})" if persona.get('source') else ""
                    all_collisions.append(f"### {persona['name']}{source_tag}\n{result}")
                except Exception as e:
                    print(f"  [Simulator] Collision failed for {persona['name']}: {e}")

    # --- Fallback: Synthetic + Google Places ---
    if not all_collisions:
        persona_count = int(os.environ.get("SYLON_PERSONA_COUNT", "1"))
        print(f"[Archaeologist] Phase 1: Generating {persona_count} synthetic archetype(s)...")
        synthetic_personas = tool_generate_synthetic_personas(
            business_description=business_description,
            location=location,
            count=persona_count
        )

        simulator_rules = f"\n{agents_config['simulator']['system_prompt']}\nOwner's scenario: \"{user_input}\""

        for persona in synthetic_personas:
            print(f"  [Simulator] Running collision for: {persona['name']}")
            try:
                result = tool_run_collision_simulation(
                    persona_narrative=persona['narrative'] + "\n\nSIMULATOR RULES:" + simulator_rules,
                    persona_drifts=persona.get('drifts', []),
                    recent_rating=persona.get('avg_rating', 3.5),
                    top_words=persona.get('top_words', []),
                    business_attributes=business_attributes
                )
                all_collisions.append(f"### {persona['name']}\n{result}")
                time.sleep(1)  # Brief buffer between calls
            except Exception as e:
                print(f"  [Simulator] Collision failed for {persona['name']}: {e}")

        # Phase 2: Google Places
        if os.environ.get("GOOGLE_PLACES_API_KEY"):
            print("[Archaeologist] Phase 2: Fetching competitor reviews from Google Places...")
            google_personas = tool_fetch_competitor_personas(
                business_category=business_description,
                location=location,
                limit=2
            )
            for persona in google_personas:
                print(f"  [Simulator] Running collision for: {persona['name']} (source: {persona.get('source', 'Google')})")
                try:
                    result = tool_run_collision_simulation(
                        persona_narrative=persona['narrative'] + "\n\nSIMULATOR RULES:" + simulator_rules,
                        persona_drifts=persona.get('drifts', []),
                        recent_rating=persona.get('avg_rating', 3.5),
                        top_words=persona.get('top_words', []),
                        business_attributes=business_attributes
                    )
                    all_collisions.append(f"### {persona['name']} (Real Review)\n{result}")
                    time.sleep(1)
                except Exception as e:
                    print(f"  [Simulator] Collision failed for {persona['name']}: {e}")

    # --- Final fallback: pre-excavated Yelp persona ---
    if not all_collisions:
        print("[Archaeologist] Falling back to pre-excavated Yelp persona...")
        persona_narrative, drifts, recent_rating, top_words = get_local_persona()
        simulator_rules = f"\n{agents_config['simulator']['system_prompt']}\nOwner's scenario: \"{user_input}\""
        result = tool_run_collision_simulation(
            persona_narrative=persona_narrative + "\n\nSIMULATOR RULES:" + simulator_rules,
            persona_drifts=drifts,
            recent_rating=recent_rating,
            top_words=top_words,
            business_attributes=business_attributes
        )
        all_collisions.append(f"### Baseline Persona\n{result}")

    # Aggregate all collision results
    combined = "\n\n---\n\n".join(all_collisions)
    return simulate_strategist(user_input, combined, painpoints)


# ---------------------------------------------------------------------------
# Master Router
# ---------------------------------------------------------------------------
def process_user_scenario(user_input: str) -> str:
    """
    Master routing function used by the FastAPI server.
    The Router classifies intent first, then dispatches to the correct pipeline.
    """
    route = evaluate_route(user_input)
    print(f"[Orchestrator] Route resolved: {route}")

    if route == "INGEST":
        return handle_ingest(user_input)
    elif route == "SIMULATE":
        return run_simulation(user_input)
    else:
        return direct_chat_strategist(user_input)


def main():
    print("Sylon Strategist Initialization...")
    print("Loaded local persona profile.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Owner: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        route = evaluate_route(user_input)

        if route == "INGEST":
            print(f"\n[OpenServ Router] -> Intent: INGEST")
            print("[OpenServ Routing] -> Parsing and ingesting reviews...\n")
            final_response = handle_ingest(user_input)
        elif route == "SIMULATE":
            print(f"\n[OpenServ Router] -> Intent: SIMULATE")
            print("[OpenServ Routing] -> Passing to Simulator with controlled hallucination rules...")
            final_response = run_simulation(user_input)
            print("[OpenServ Routing] -> Sending Simulator result to Strategist...\n")
        else:
            print(f"\n[OpenServ Router] -> Intent: CHAT")
            print("[OpenServ Routing] -> Responding conversationally...\n")
            final_response = direct_chat_strategist(user_input)

        print(f"Sylon: {final_response}\n")

if __name__ == "__main__":
    main()
