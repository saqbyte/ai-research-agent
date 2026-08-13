from openai import (
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    RateLimitError,
)

from src.config import (
    MODEL_NAME,
    get_openai_client
)

from src.logger import get_logger
from src.models import ResearchPlan
from src.prompts import PLANNER_INSTRUCTIONS


logger = get_logger(__name__)


def create_research_plan(
    topic: str
) -> ResearchPlan:

    topic = topic.strip()

    if not topic:

        logger.warning(
            "Empty research topic received."
        )

        raise ValueError(
            "Research topic cannot be empty."
        )

    logger.info(
        "Creating research plan."
    )

    client = get_openai_client()

    try:

        response = client.responses.parse(
            model=MODEL_NAME,
            instructions=PLANNER_INSTRUCTIONS,
            input=topic,
            text_format=ResearchPlan
        )

    except AuthenticationError:

        logger.error(
            "OpenAI authentication failed "
            "during planning."
        )

        raise RuntimeError(
            "Authentication with OpenAI failed. "
            "Check your API key."
        )

    except RateLimitError:

        logger.error(
            "OpenAI rate limit reached "
            "during planning."
        )

        raise RuntimeError(
            "OpenAI rate limit reached. "
            "Please try again later."
        )

    except APITimeoutError:

        logger.error(
            "Planner request timed out."
        )

        raise RuntimeError(
            "The planner request timed out. "
            "Please try again."
        )

    except APIConnectionError:

        logger.error(
            "Could not connect to OpenAI "
            "during planning."
        )

        raise RuntimeError(
            "Could not connect to OpenAI. "
            "Check your internet connection."
        )

    except BadRequestError as error:

        logger.error(
            "Planner request was rejected."
        )

        raise RuntimeError(
            f"Planner request failed: {error}"
        )

    plan = response.output_parsed

    if plan is None:

        logger.error(
            "Planner returned no structured output."
        )

        raise RuntimeError(
            "Planner did not return "
            "a structured research plan."
        )

    logger.info(
        "Research plan created with %s steps.",
        len(plan.steps)
    )

    return plan