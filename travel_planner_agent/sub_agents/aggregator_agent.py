
from google.adk.agents import Agent
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

aggregator_agent_instruction="""Combine these two findings into a single executive summary:

    **Flight itineraries:**
    {flight_search_findings}
    
    **Hotel Reservation:**
    {hotel_reservations}
    
    Your summary should highlight the what the user should pay attention to."""     


# The AggregatorAgent runs *after* the parallel step to synthesize the results.
# Use Agent instead of LLMAgent as a workflow Agent to orchestrate the execution of other agents.  It "enforce" a more deterministic result. 
aggregator_agent = Agent(
    name="AggregatorAgent",
    model=config.model,
    # It uses placeholders to inject the outputs from the parallel agents, which are now in the session state.
    instruction="""Combine these three findings into a single executive summary:

    **Flight itineraries:**
    {flight_search_findings}
    
    **Hotel Reservation:**
    {hotel_reservations}
    
    Your summary should highlight the what the user should pay attention to.""",
    output_key="executive_summary",  # This will be the final output of the entire system.
)
