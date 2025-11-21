from google.genai import types
from google.adk.models.google_llm import Gemini


class TravelPlannerConfiguration:
    """Configuration for travel planner models and parameters.

    Attributes:
        worker_model (str): Model for working/generation tasks.
        retry_config (types.HttpRetryOptions): Maximum model retry configuration allowed.
        model (Gemini): actuall model created
    """

    worker_model: str = "gemini-2.5-flash-lite"
    retry_config=types.HttpRetryOptions(
        attempts=5,  # Maximum retry attempts
        exp_base=7,  # Delay multiplier
        initial_delay=1,
        http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
    )
        
    model: Gemini = Gemini(
        model= worker_model,
        retry_options=retry_config
    )
    
config = TravelPlannerConfiguration()

