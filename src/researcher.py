from src.config import (
    MODEL_NAME,
    get_openai_client
)

from src.prompts import (
    RESEARCHER_INSTRUCTIONS
)


def execute_research(topic, plan):
    """
    Execute a research plan using web search.
    """

    if not topic:
        raise ValueError(
            "Research topic cannot be empty."
        )

    if not plan:
        raise ValueError(
            "Research plan cannot be empty."
        )

    client = get_openai_client()

    research_input = f"""
Research Request:

{topic}


Research Plan:

{plan}


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