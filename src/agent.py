from src.logger import get_logger
from src.planner import create_research_plan
from src.researcher import execute_research


logger = get_logger(__name__)


def research_agent(
    topic: str
):

    topic = topic.strip()

    if not topic:

        logger.warning(
            "Research workflow received "
            "an empty topic."
        )

        raise ValueError(
            "Please provide a research topic."
        )

    logger.info(
        "Research workflow started."
    )

    logger.info(
        "Topic received: %s",
        topic
    )

    plan = create_research_plan(
        topic
    )

    report = execute_research(
        topic,
        plan
    )

    logger.info(
        "Research workflow completed."
    )

    return {
        "topic": topic,
        "plan": plan,
        "report": report
    }