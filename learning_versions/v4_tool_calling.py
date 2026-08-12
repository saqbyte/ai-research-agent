import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def search_web(query):
    """
    Temporary search tool.
    We'll connect this to real wen search later.
    """
    print("\nTool Connected")
    print(f"Query: {query}")

    return {
        "query": query,
        "results": [
            "AI automation is increasingly being adopted by small businesses.",
            "Common use cases include customer support, marketing, and lead generation.",
            "Businesses are using AI to automate repetitive tasks."
        ]
    }


tools =[
    {
    "type": "function",
    "name": "search_web",
    "description": "Search the information on the internet related to research topic",
    "parameters":{
         "type": "object",
         "properties": {
             "query": {
                 "type": "string",
                 "description": "The search query to use."
             }
         }
         ,
         "required": ["query"],
         "additionalProperties": False
    }
    }
]

def research_agent(topic):
    print(f"Research Request: {topic}")
    response = client.responses.create(
        model="gpt-5-mini",
        instructions=
        f"""
        You are a research agent.
        The user wants to research: {topic}
        if you need external information, use the search_web tool.
        """,
        input=topic,
        tools=tools,
        tool_choice="required"
    )

    print("\n===== RAW RESPONSE =====")
    print(response)
    print("========================")

    

    for item in response.output:
        print(item.type)
        if item.type== "function_call":
            print("Agent requested a tool")
            print(item.name)

            arguments = json.loads(item.arguments)

            if item.name== "search_web":
                result = search_web(arguments["query"])
                print("\nTool Result:")
                print(result)

topic = input("What should I research? ")

research_agent(topic)