from src.config import (
    MODEL_NAME,
    get_openai_client
)

from src.models import ResearchPlan

from src.prompts import (
    PLANNER_INSTRUCTIONS
)


def create_research_plan(
    topic: str
) -> ResearchPlan:
    """
    Generate a structured research plan.

    Args:
        topic:
            User's research request.

    Returns:
        ResearchPlan:
            Parsed and validated research plan.
    """

    topic = topic.strip()

    if not topic:
        raise ValueError(
            "Research topic cannot be empty."
        )

    client = get_openai_client()

    response = client.responses.parse(
        model=MODEL_NAME,

        instructions=PLANNER_INSTRUCTIONS,

        input=topic,

        text_format=ResearchPlan
    )

    plan = response.output_parsed

    if plan is None:
        raise RuntimeError(
            "Planner did not return "
            "a structured research plan."
        )

    return plan