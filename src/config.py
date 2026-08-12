import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


MODEL_NAME = os.getenv(
    "OPENAI_MODEL",
    "gpt-5-mini"
)


def get_openai_client():
    """
    Create and return the OpenAI client.

    Raises:
        RuntimeError:
            If OPENAI_API_KEY is not configured.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is missing. "
            "Add it to your .env file."
        )

    return OpenAI(
        api_key=api_key
    )