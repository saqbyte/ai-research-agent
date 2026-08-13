from unittest.mock import (
    MagicMock,
    patch
)

import pytest

from src.models import ResearchPlan
from src.planner import create_research_plan


def test_planner_rejects_empty_topic():

    with pytest.raises(ValueError):

        create_research_plan("")


@patch(
    "src.planner.get_openai_client"
)
def test_planner_returns_structured_plan(
    mock_get_client
):

    fake_plan = ResearchPlan(
        objective="Research AI automation.",
        steps=[
            "Research the market.",
            "Identify opportunities."
        ]
    )

    mock_response = MagicMock()

    mock_response.output_parsed = (
        fake_plan
    )

    mock_client = MagicMock()

    mock_client.responses.parse.return_value = (
        mock_response
    )

    mock_get_client.return_value = (
        mock_client
    )

    result = create_research_plan(
        "AI automation"
    )

    assert result == fake_plan

    mock_client.responses.parse.assert_called_once()


@patch(
    "src.planner.get_openai_client"
)
def test_planner_rejects_empty_output(
    mock_get_client
):

    mock_response = MagicMock()

    mock_response.output_parsed = None

    mock_client = MagicMock()

    mock_client.responses.parse.return_value = (
        mock_response
    )

    mock_get_client.return_value = (
        mock_client
    )

    with pytest.raises(
        RuntimeError,
        match="structured research plan"
    ):

        create_research_plan(
            "AI automation"
        )