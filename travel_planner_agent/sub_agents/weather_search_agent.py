# Create image agent with MCP integration

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset, StreamableHTTPConnectionParams


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


# Point to your MCP Weather server
weather_toolset = McpToolset(
    connection_params=StreamableHTTPConnectionParams(url="http://localhost:8180/mcp")
)


weather_search_agent_instruction="""
    You are the weather_agent. Your task is to retrieve the weather forecast for the user’s travel destination for the full duration of their stay.

    Follow these steps:
    1. Identify the destination city from the user's itinerary.
    2. Identify the departure date and the return date of the user's stay.
    3. Query the MCP Weather Server using the `weather_toolset` tool:
        - city: the destination city
        - date_range: the full period between the departure date and the return date
    4. Return a clear, friendly weather summary to the user, including:
        - daily temperature ranges
        - precipitation probability
        - any special alerts (extreme heat, storms, etc.)
        - suggestions on what to pack
    """

weather_search_agent = LlmAgent(
    name="WeatherSearchAgent",
    model=config.model,
    instruction=weather_search_agent_instruction,
    tools=[weather_toolset],
    output_key="destination_weather",  # The result of this agent will be stored in the session state with this key.
)
