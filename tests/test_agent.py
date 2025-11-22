import asyncio
import sys
import io

from google.adk.runners import InMemoryRunner
from google.adk.plugins.logging_plugin import LoggingPlugin
from travel_planner_agent.agent import root_agent


sample_user_prompt = "Plan a trip from Toronto to Tokyo for 5 days for a family of 4.  Departure date is 1st December 2025.  Return date is 5th December 2025."


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
