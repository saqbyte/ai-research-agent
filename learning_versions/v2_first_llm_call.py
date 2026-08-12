import os
#import logging
from dotenv import load_dotenv
from openai import OpenAI

#logging.basicConfig(level=logging.DEBUG)
load_dotenv()

# Read the API key from environment variable name as a string
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-4o-mini",
    input="Classify 'quantum computing' into one of these categories: AI, Finance, Technology, Business, Unknown. Return only the category."
)

print(response.output_text)