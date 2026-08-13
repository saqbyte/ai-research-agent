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
from src.prompts import RESEARCHER_INSTRUCTIONS


logger = get_logger(__name__)


def execute_research(
    topic: str,
    plan: ResearchPlan
) -> str:
    """
    Execute a structured research plan
    using web search.
    """

    topic = topic.strip()

    if not topic:

        logger.warning(
            "Empty research topic received."
        )

        raise ValueError(
            "Research topic cannot be empty."
        )

    if not plan.steps:

        logger.warning(
            "Research plan contains no steps."
        )

        raise ValueError(
            "Research plan has no steps."
        )

    formatted_steps = "\n".join(
        f"{index}. {step}"
        for index, step in enumerate(
            plan.steps,
            start=1
        )
    )

    research_input = f"""
Research Request:

{topic}


Research Objective:

{plan.objective}


Research Steps:

{formatted_steps}


Execute this research plan now.

Do not create another plan.

Use web research to gather reliable evidence.

When sufficient reliable evidence has been collected,
answer the user's research request.

Follow the source-quality and evidence rules from
your system instructions.

Do not create another research plan.
"""

    logger.info(
        "Starting research execution."
    )

    client = get_openai_client()

    try:

        response = client.responses.create(
            model=MODEL_NAME,
            instructions=RESEARCHER_INSTRUCTIONS,
            input=research_input,
            tools=[
                {
                    "type": "web_search"
                }
            ]
        )

    except AuthenticationError:

        logger.error(
            "OpenAI authentication failed "
            "during research."
        )

        raise RuntimeError(
            "Authentication with OpenAI failed. "
            "Check your API key."
        )

    except RateLimitError:

        logger.error(
            "OpenAI rate limit reached "
            "during research."
        )

        raise RuntimeError(
            "OpenAI rate limit reached. "
            "Please try again later."
        )

    except APITimeoutError:

        logger.error(
            "Research request timed out."
        )

        raise RuntimeError(
            "The research request timed out. "
            "Please try again."
        )

    except APIConnectionError:

        logger.error(
            "Could not connect to OpenAI "
            "during research."
        )

        raise RuntimeError(
            "Could not connect to OpenAI. "
            "Check your internet connection."
        )

    except BadRequestError as error:

        logger.error(
            "Research request was rejected."
        )

        raise RuntimeError(
            f"Research request failed: {error}"
        )

    report = response.output_text

    if not report:

        logger.error(
            "Researcher returned an empty report."
        )

        raise RuntimeError(
            "Researcher returned an empty report."
        )

    logger.info(
        "Research completed successfully."
    )

    return report.strip()