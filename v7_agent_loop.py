import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def calculator(expression):
    print("\nCalculator Tool:")
    print(f"Expression: {expression}")

    result = eval(
        expression,
        {"__builtins__": {}},
        {}
    )

    return {
        "expression": expression,
        "result": result
    }


tools = [
    {
        "type": "web_search"
    },
    {
        "type": "function",
        "name": "calculator",
        "description": "Calculate a mathematical expression.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Mathematical expression to calculate."
                }
            },
            "required": ["expression"],
            "additionalProperties": False
        }
    }
]


def execute_tool(name, arguments):

    if name == "calculator":
        return calculator(arguments["expression"])

    return {
        "error": f"Unknown tool: {name}"
    }


def research_agent(topic):

    print(f"\nResearch Request: {topic}")

    # This list represents the growing conversation/state.
    input_list = [
        {
            "role": "user",
            "content": topic
        }
    ]

    max_iterations = 10

    for iteration in range(1, max_iterations + 1):

        print(f"\n# Agent Iteration: {iteration}")

        response = client.responses.create(
            model="gpt-5-mini",

            instructions="""
You are a research agent.

Use web search for current or external information.

Use the calculator when an exact mathematical
calculation is required.

Use tools only when necessary.

If you already have enough information,
provide the final answer instead of calling
the same tool again.
""",

            input=input_list,
            tools=tools
        )

        # VERY IMPORTANT:
        # preserve everything the model just returned
        input_list += response.output

        function_calls = [
            item
            for item in response.output
            if item.type == "function_call"
        ]

        for item in response.output:
            print(f"Output type: {item.type}")

        # No custom function calls = model is done
        if not function_calls:

            if response.output_text:
                print("\n==============================")
                print("FINAL ANSWER")
                print("==============================")

                print(response.output_text)

            return

        # Execute all requested custom tools
        for tool_call in function_calls:

            print(f"\nTool Requested: {tool_call.name}")

            arguments = json.loads(
                tool_call.arguments
            )

            print(f"Arguments: {arguments}")

            result = execute_tool(
                tool_call.name,
                arguments
            )

            print("Tool Result:")
            print(result)

            # Attach result to the matching function call
            input_list.append(
                {
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": json.dumps(result)
                }
            )

    print(
        "\nAgent stopped because the maximum "
        "number of iterations was reached."
    )


topic = input("Research For: ")

research_agent(topic)