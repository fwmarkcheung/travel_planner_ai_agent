from google.adk.agents import LlmAgent
from google.adk.tools import google_search


# Handle imports for both script execution and module import
try:
    # Try relative import first (when used as a module)
    from ..config import config
  
except ImportError:
    # Fall back to absolute import (when run as a script)
    import sys
    import os
    # Add the project root to sys.path to enable absolute imports
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from travel_planner_agent.config import config


hotel_search_agent_instruction="""You are a specialized hotel reservation agent. Your only job is to find the hotel reservations using the information provided by the user.

    You MUST ALWAYS use google_search tool to search and provide the reservations in a clear and concise format for the following options:
    
    1. The Cheapest reservation.
    2. The most luxury reservation.
    3. The most convenient reservation.
     """

hotel_search_agent = LlmAgent(
    name="HotelSearchAgent",
    model=config.model,
    instruction=hotel_search_agent_instruction,
    tools=[google_search],
    output_key="hotel_reservations",  # The result of this agent will be stored in the session state with this key.
)

