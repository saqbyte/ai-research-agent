from src.config import (
    MODEL_NAME,
    get_openai_client
)

from src.prompts import (
    PLANNER_INSTRUCTIONS
)


def create_research_plan(topic):
    """
    Generate a research plan for a topic.

    Args:
        topic: User's research request.

    Returns:
        Research plan as text.
    """

    if not topic:
        raise ValueError(
            "Research topic cannot be empty."
        )

    client = get_openai_client()

    response = client.responses.create(
        model=MODEL_NAME,

        instructions=(
            PLANNER_INSTRUCTIONS
        ),

        input=topic
    )

    plan = response.output_text

    if not plan:
        raise RuntimeError(
            "Planner returned an empty response."
        )

    return plan.strip()