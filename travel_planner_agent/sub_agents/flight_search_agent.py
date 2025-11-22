
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


flight_search_agent_instruction="""
    You are a specialized flight service agent. Your only job is to find the flights itinerary using the information provided by the user.

    You MUST use the google_search tool to provide the flight itinerary in a clear and concise format for the following options:
    
    1. The cheapest flight.
    2. The fastest flight.
    3. The most convenient flight.
    """


flight_search_agent = LlmAgent(
    name="FlightSearchAgent",
    model=config.model,
    instruction=flight_search_agent_instruction,
    tools=[google_search],
    output_key="flight_search_findings",  # The result of this agent will be stored in the session state with this key.
)
