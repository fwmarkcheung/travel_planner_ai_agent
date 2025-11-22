# Handle imports for both script execution and module import
try:
    # Try relative import first (when used as a module)
    from .sub_agents import (
        flight_search_agent,
        hotel_search_agent,
        weather_search_agent,
        aggregator_agent,
    )
  
except ImportError:
    # Fall back to absolute import (when run as a script)
    from sub_agents import (
        flight_search_agent,
        hotel_search_agent,
        weather_search_agent,
        aggregator_agent,
    )

from google.adk.agents import SequentialAgent, ParallelAgent
from google.adk.runners import InMemoryRunner
from google.adk.plugins.logging_plugin import (
    LoggingPlugin,
)  # <---- 1. Import the Plugin

import logging
import os
import asyncio


''' 
    This is a trip planner agent.  
    Given a user trip request, it plans a trip and provide the following information for the cheapest, most convenient, and most luxary options:
    1. Flight itinearies
    2. Hotel reservations
    3. Weather report to suggest the appropriate clothing

'''
# Configure logging with DEBUG log level.
logging.basicConfig(
    filename="logger.log",
    level=logging.DEBUG,
    format="%(filename)s:%(lineno)s %(levelname)s:%(message)s",
)

# The ParallelSearchTeam runs all its sub-agents simultaneously.
parallel_planner_team = ParallelAgent(
    name="ParallelSearchTeam",
    sub_agents=[flight_search_agent, hotel_search_agent, weather_search_agent],
)

# This SequentialAgent defines the high-level workflow: run the parallel team first, then run the aggregator.
root_agent = SequentialAgent(
    name="TripPlannerAgent",
    sub_agents=[parallel_planner_team, aggregator_agent],
)