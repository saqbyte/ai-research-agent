import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def search_web(query):
    """
    This is our first tool.

    For now, it is a simulated search tool.
    Later, we'll connect it to a real web search API.
    """
    print(f"\nSearch tool called")
    print(f"Searching the web for: {query}")

def research_agent(topic):
    print(f"Research request: {topic}")
    response = client.responses.create(
        model="gpt-5-mini",
        instructions="""
        You are a research planning assistant.

        Your job is to convert the user's research request
        into ONE concise web search query.

        Rules:
        - Return ONLY the search query.
        - Do not explain anything.
        - Do not ask questions.
        - Do not use bullet points.
        - Keep the query under 15 words.        
        """,
        input = topic
    )
    search_query = response.output_text.strip()

    print(f"\nAgent decided to search for:")
    print(search_query)

    results = search_web(search_query)

    print(f"\nTool returned:")
    print(results)

    

topic = input("What should I research?\n")
research_agent(topic)
