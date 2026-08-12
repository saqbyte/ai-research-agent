import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def research_agent(topic):
    print(f"Research Request: {topic}")
    response = client.responses.create(
        model="gpt-5-mini",
        tools=[{ "type": "web_search" }],
        instructions="""
You are a research agent.

Research the user's topic using web search.

Use reliable sources whenever possible.

Provide:
1. A concise overview
2. Important facts
3. Key statistics when available
4. Major findings
5. Sources

Clearly distinguish between established facts
and uncertain information.
""",
        input=topic
        
    )
    print("\n============================================")
    print("Final Research Report")
    print(response.output_text)

topic = input("Research For:\n")
research_agent(topic)