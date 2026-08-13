from src.config import (
    MODEL_NAME,
    get_openai_client
)

from src.models import ResearchPlan

from src.prompts import (
    RESEARCHER_INSTRUCTIONS
)


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
        raise ValueError(
            "Research topic cannot be empty."
        )

    if not plan.steps:
        raise ValueError(
            "Research plan has no steps."
        )

    client = get_openai_client()

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

When sufficient information has been collected,
produce the final research report.
"""

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

    report = response.output_text

    if not report:
        raise RuntimeError(
            "Researcher returned an empty report."
        )

    return report.strip()