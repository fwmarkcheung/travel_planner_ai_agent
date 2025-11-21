# travel_planner_ai_agent
 Travel planner AI agent built using Google ADK

### Problem Statement

Planning trip manually is laborious because it requires significant time in looking up flight itineraries, hotel booking, weather in the destination, and etc

Automation can streamline findings and recommend a trip plan.  This saves the time for the user to plain the trip.

### Solution Statement

Agents can automatically search flight itineraries, hotel booking, weather in the destination, and etc and help the user to plan the trip much more efficiently.  It can generate initial trip plan and give the user an idea the estimated cost for a cheap, a convenient, and luxary options.



### Value Statement

The travel planner agent reduced my time per trip planning, suggesting options for cheap, convenient, and luxary trip, and thus, help me to plan a trip much more efficiently.

### Enhancement

If I had more time I would ...

## Installation



### Running the Agent in ADK Web mode

From the command line of the working directory execute the following command. 



```bash
adk web
```

### Features

- Multi-agent system, including any combination of:
		Agent powered by an LLM
		Parallel agents
		Sequential agents

- Tools:
		built-in tools using Google Search

- Observability: Logging, Tracing, Metrics

The following diagram shows how workflow and 
Image:

![multi-agents-architecture](multi-agents-architecture.jpg)

### Features

- Multi-agent system, including any combination of:
		Agent powered by an LLM
		Parallel agents
		Sequential agents

- Tools:
		built-in tools using Google Search

- Observability: Logging, Tracing, Metrics

### Agent Architecture

![multi-agents-architecture](multi-agents-architecture.jpg)

- FlightSearchAgent - LLM Agent uses google search tool to provide flight itineraries
- HotelSearchAgent - LLM Agent uses google search tool to provide hotel booking recommendations
- ParallelSearchTeam - create a search team and delegate the search task to the corresponding agents to perform the task in parallel
- AggregatorAgent - Summarize the recommendations from the above agents
- TripPlannerAgent - a root agent works a high-level orchestrator to delegate the user request to the above agents 
