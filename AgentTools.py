# Define which tools the agent can use to answer user queries
search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    )
]
