import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Read the API key from environment variable name as a string
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def classify_topic(topic):
    """
    This function classifies a given topic into one of the predefined categories.
    It uses the OpenAI API to perform the classification.
    """
    response = client.responses.create(
        model="gpt-4o-mini",
        input=f"Classify '{topic}' into one of these categories: AI, Finance, Technology, Business, Unknown. Return only the category."
    )
    return response.output_text.strip()


def research_agent(topic):
    """
    This function represents a research agent that performs research tasks.
    It can be expanded to include specific research functionalities as needed.
    """
    # Placeholder for research logic
    print(f"Research topic: {topic}")
    category = classify_topic(topic)
    print(f"Classified as: {category}")

    if category == "AI":
        print("Searching for Artificial Intelligence resources...")
    elif category == "Stock":
        print("Searching for stock market resources...")
    elif category == "Finance":
        print("Searching for finance resources...")
    elif category == "Technology":
        print("Searching for Technology resources...")
    elif category == "Business":
        print("Searching for Business resources...")
    else:
        print(f"Searching for resources related to {topic}...")

topic = input("Enter a topic to research: ")
research_agent(topic)