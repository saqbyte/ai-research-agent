from src.planner import (
    create_research_plan
)

from src.researcher import (
    execute_research
)


def research_agent(topic: str):
    """
    Run the complete research workflow.
    """

    topic = topic.strip()

    if not topic:
        raise ValueError(
            "Please provide a research topic."
        )

    plan = create_research_plan(
        topic
    )

    report = execute_research(
        topic,
        plan
    )

    return {
        "topic": topic,
        "plan": plan,
        "report": report
    }