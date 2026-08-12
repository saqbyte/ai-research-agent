
import os
from dotenv import load_dotenv
import json
from openai import OpenAI

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def calculator(expression):
    """
    Calculate a mathematical expression.

    Example:
            calculator("125000*0.18")
    """
    print("Calculator Tool:")

    # Temporary learning implementation.
    # We will make this safer later.
    result = eval(expression, {"__builtins__": {}}, {})

    return {
        "expression":expression,
        "result":result
    }

tools = [
    {
        "type":"web_search"
    },
    {
        "type":"function",
        "name":"calculator",
        "description":"Calculate a mathematical expression",
        "parameters":{
            "type":"object",
            "properties":{
                "expression":{
                    "type":"string",
                    "description":"Mathematical expression to calculate"
                }
            },
                
            "required":["expression"],
            "additionalProperties": False
        }
    }
]


def research_agent(topic):
    print(f"Research Request: {topic}")

    response = client.responses.create(

        model="gpt-5-mini",
        instructions="""
You are research agent.

You have access to two tools.

1. Web Search: Use this for current or external information.

2. Calculator: Use this to calculate mathematical expression.

Choose the appropriate tool when necessary.

After recieving tool results, provide a clear final answer.
""",
        input=topic,
        tools=tools,
        )

    print("\n==================================")
    print("MODEL OUTPUT")
    print("\n==================================")

    for item in response.output:
        print(f"Output type: {item.type}")
        if item.type== "function_call":
            print(f"Tool Requested: {item.name}")
            arguments = json.loads(item.arguments)
            if item.name== "calculator":
                result = calculator(arguments["expression"])
                print("\nTools Result:")
                print(result)

                #send result back to LLM model

                response = client.responses.create(
                    model="gpt-5-mini",
                    instructions="""
                    Use the calculator result to answer the user's question appropriately
                    """,
                    previous_response_id=response.id,
                    input=[{
                        "type":"function_call_output",
                        "call_id": item.call_id,
                        "output":json.dumps(result)
                    
                        }]
                )
                print("\n==============================")
                print("FINAL ANSWER")
                print("==============================")

                print(response.output_text)


topic = input("Research For: ")

research_agent(topic)

    

