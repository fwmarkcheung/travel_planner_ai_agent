

from google.adk.agents import Agent

from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search, AgentTool, ToolContext
from google.adk.code_executors import BuiltInCodeExecutor


from google.genai import types

retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)

#from config import retry_config
#retry_config=retry_config.retry_config

aggregator_agent_instruction="""Combine these two findings into a single executive summary:

    **Flight itineraries:**
    {flight_search_findings}
    
    **Hotel Reservation:**
    {hotel_reservations}
    
    Your summary should highlight the what the user should pay attention to."""     


# The AggregatorAgent runs *after* the parallel step to synthesize the results.
aggregator_agent = Agent(
    name="AggregatorAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    # It uses placeholders to inject the outputs from the parallel agents, which are now in the session state.
    instruction="""Combine these three findings into a single executive summary:

    **Flight itineraries:**
    {flight_search_findings}
    
    **Hotel Reservation:**
    {hotel_reservations}
    
    Your summary should highlight the what the user should pay attention to.""",
    output_key="executive_summary",  # This will be the final output of the entire system.
)
