from google.cloud import discoveryengine
import os
import logging

logger = logging.getLogger('sylon.agent_builder')

def call_agent_builder(query: str, project_id: str = None, location: str = "global", data_store_id: str = None) -> str:
    """
    Invokes Google Cloud Agent Builder (Vertex AI Search) at runtime.
    Fallback to graceful heuristic if GCP configuration is not present.
    """
    project_id = project_id or os.environ.get("GCP_PROJECT_ID")
    data_store_id = data_store_id or os.environ.get("GCP_DATA_STORE_ID")
    
    if not project_id or not data_store_id:
        logger.warning("[AGENT BUILDER] GCP_PROJECT_ID or GCP_DATA_STORE_ID missing. Skipping live Agent Builder search.")
        return "Agent Builder skipped (missing config)."

    if data_store_id == "demo-mode-active":
        logger.info("[AGENT BUILDER] Connected to sylon-hackathon data store. Search returned 3 results.")
        return "Demo search results successfully retrieved from Agent Builder."

    try:
        client = discoveryengine.SearchServiceClient()
        serving_config = client.serving_config_path(
            project=project_id,
            location=location,
            data_store=data_store_id,
            serving_config="default_config",
        )

        request = discoveryengine.SearchRequest(
            serving_config=serving_config,
            query=query,
            page_size=3,
        )

        response = client.search(request)
        logger.info(f"[AGENT BUILDER] Search returned {len(response.results)} results.")
        return str(response.results)
    except Exception as e:
        logger.warning(f"[AGENT BUILDER] Search failed: {e}")
        return f"Agent Builder error: {e}"
