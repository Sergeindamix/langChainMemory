# Define which tools the agent can use to answer user queries
search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    )
]

def duck_wrapper(input_text):
    search_results = search.run(f"site:webmd.com {input_text}")
    return search_results

tools = [
    Tool(
        name = "Search WebMD",
        func=duck_wrapper,
        description="useful for when you need to answer medical and pharmalogical questions"
    )
]
