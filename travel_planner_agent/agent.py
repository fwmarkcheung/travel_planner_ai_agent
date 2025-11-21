# Handle imports for both script execution and module import
try:
    # Try relative import first (when used as a module)
    from .sub_agents import (
        flight_search_agent,
        hotel_search_agent,
        aggregator_agent,
    )
except ImportError:
    # Fall back to absolute import (when run as a script)
    from sub_agents import (
        flight_search_agent,
        hotel_search_agent,
        aggregator_agent,
    )


''' 
    This is a trip planner agent.  
    Given a user plan request, it will plan the trip and provide the following information:
    1. Flight itinearies
    2. Hotel reservations
    3. Weather report to suggest the appropriate clothing
    4. Visa requirement
    5. Transporation recommendations

'''

sample_user_prompt = "Plan a trip from Toronto to Tokyo for 5 days for a family of 4.  Departure date is 1st December 2025.  Return date is 5th December 2025."





from google.adk.agents import Agent, SequentialAgent, ParallelAgent
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search, AgentTool, ToolContext
from google.adk.code_executors import BuiltInCodeExecutor
from google.genai import types

from google.adk.plugins.logging_plugin import (
    LoggingPlugin,
)  # <---- 1. Import the Plugin

import logging
import os

import asyncio



# Clean up any previous logs
for log_file in ["logger.log", "web.log", "tunnel.log"]:
    if os.path.exists(log_file):
        os.remove(log_file)
        print(f"Cleaned up {log_file}")

# Configure logging with DEBUG log level.
logging.basicConfig(
    filename="logger.log",
    level=logging.DEBUG,
    format="%(filename)s:%(lineno)s %(levelname)s:%(message)s",
)

# The ParallelSearchTeam runs all its sub-agents simultaneously.
parallel_planner_team = ParallelAgent(
    name="ParallelSearchTeam",
    sub_agents=[flight_search_agent, hotel_search_agent],
)

# This SequentialAgent defines the high-level workflow: run the parallel team first, then run the aggregator.
root_agent = SequentialAgent(
    name="TripPlannerAgent",
    sub_agents=[parallel_planner_team, aggregator_agent],
)


async def run_trip_planner():
    runner = InMemoryRunner(agent=root_agent,
    plugins=[
        LoggingPlugin()
    ],  # <---- 2. Add the plugin. Handles standard Observability logging across ALL agents
    )
    
    response = await runner.run_debug(sample_user_prompt)
    return response


if __name__ == "__main__":
    asyncio.run(run_trip_planner())
