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

hotel_search_agent_instruction="""You are a specialized hotel reservation agent. Your only job is to find the hotel reservations using the information provided by the user.

    You MUST ALWAYS use google_search tool to search and provide the reservations in a clear and concise format for the following options:
    
    1. The Cheapest reservation.
    2. The most luxury reservation.
    3. The most convenient reservation.
     """






    #instruction="""You are a specialized reservation service agent. Your only job is to use the
    #google_search tool to find the reservations itinerary using the information provided by the user.
    #The information provided by the user is: {user_input}

    #Provide the reservation itinerary in a clear and concise format for the following options:
    #1. Cheapest reservation.
    #2. Fastest reservation.
    #3. Most convenient reservation.
    # """   


hotel_search_agent = LlmAgent(
    name="HotelSearchAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""You are a specialized hotel reservation agent. Your only job is to use the
    google_search tool to find the hotel reservations using the information provided by the user.
    

    Provide the reservations in a clear and concise format for the following options:
    
    1. Cheapest reservation.
    2. Fastest reservation.
    3. Most convenient reservation.
     """,
    tools=[google_search],
    output_key="hotel_reservations",  # The result of this agent will be stored in the session state with this key.
)

