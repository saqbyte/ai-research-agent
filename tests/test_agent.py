from unittest.mock import patch

import pytest

from src.agent import research_agent
from src.models import ResearchPlan


def test_agent_rejects_empty_topic():

    with pytest.raises(ValueError):

        research_agent("")


@patch("src.agent.execute_research")
@patch("src.agent.create_research_plan")
def test_agent_workflow(
    mock_create_plan,
    mock_execute_research
):

    fake_plan = ResearchPlan(
        objective="Research AI automation.",
        steps=[
            "Research the market.",
            "Identify opportunities."
        ]
    )

    mock_create_plan.return_value = fake_plan

    mock_execute_research.return_value = (
        "Final research report."
    )

    result = research_agent(
        "AI automation"
    )

    assert result["topic"] == (
        "AI automation"
    )

    assert result["plan"] == fake_plan

    assert result["report"] == (
        "Final research report."
    )

    mock_create_plan.assert_called_once_with(
        "AI automation"
    )

    mock_execute_research.assert_called_once_with(
        "AI automation",
        fake_plan
    )