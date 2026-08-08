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
    We'll connect this to real when search later.
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
    print(f"Reaserch Request: {topic}")

    response = client.responses.create(
        model="gpt-5-mini",
        instructions=
        """
You are research agent.
Research the user's topic.
If external information is required,
use the search_web() tool.
After recieving search results,
analyze them and provide a concise research summary.
""",
        input=topic,
        tool_choice="required",
        tools=tools

    )
    #print(response.output)

# Process model output
    for item in response.output:
        print(f"\nModel output type: {item.type}")
        if item.type== "function_call":
            print(f"Agent Requested: {item.name}")
            arguments = json.loads(item.arguments)
            print(arguments)
            if item.name == "search_web":
                result = search_web(arguments["query"])
                print(f"Result:\n{result}")

                #Send tool request back to model
                response = client.responses.create(
                    model="gpt-5-mini",
                    previous_response_id=response.id,
                    instructions="""
You are research agent.
Analyze the search results and answer the user's
research question clearly.

Do not claim information that is not supported
by the provided search results.
""",
                    input=[
                        {
                            "role":"user",
                            "content":topic
                        },
                        {
                            "type":"function_call_output",
                            "call_id":item.call_id,
                            "output":json.dumps(result)
                        }
                    ]
                )

                print("\n==============================")
                print("FINAL RESEARCH REPORT")
                print("==============================")

                print(response.output_text)
            


topic = input("Search for:")
research_agent(topic)