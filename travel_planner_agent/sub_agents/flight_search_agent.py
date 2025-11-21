
from google.adk.agents import LlmAgent
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


flight_search_agent_instruction="""You are a specialized flight service agent. Your only job is to find the flights itinerary using the information provided by the user.

    You MUST ALWAYS use the google_search tool to provide the flight itinerary in a clear and concise format for the following options:
    
    1. The cheapest flight.
    2. The fastest flight.
    3. The most convenient flight.
    """


retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)

model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
        )



flight_search_agent = LlmAgent(
    name="FlightSearchAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction=flight_search_agent_instruction,
    tools=[google_search],
    output_key="flight_search_findings",  # The result of this agent will be stored in the session state with this key.
)
