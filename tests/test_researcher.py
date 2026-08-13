from unittest.mock import (
    MagicMock,
    patch
)

import pytest

from src.models import ResearchPlan
from src.researcher import execute_research


def create_fake_plan():

    return ResearchPlan(
        objective="Research AI automation.",
        steps=[
            "Research the market.",
            "Identify opportunities."
        ]
    )


def test_researcher_rejects_empty_topic():

    plan = create_fake_plan()

    with pytest.raises(ValueError):

        execute_research(
            "",
            plan
        )


@patch(
    "src.researcher.get_openai_client"
)
def test_researcher_returns_report(
    mock_get_client
):

    plan = create_fake_plan()

    mock_response = MagicMock()

    mock_response.output_text = (
        "AI automation research results."
    )

    mock_client = MagicMock()

    mock_client.responses.create.return_value = (
        mock_response
    )

    mock_get_client.return_value = (
        mock_client
    )

    result = execute_research(
        "AI automation",
        plan
    )

    assert result == (
        "AI automation research results."
    )

    mock_client.responses.create.assert_called_once()


@patch(
    "src.researcher.get_openai_client"
)
def test_researcher_rejects_empty_report(
    mock_get_client
):

    plan = create_fake_plan()

    mock_response = MagicMock()

    mock_response.output_text = ""

    mock_client = MagicMock()

    mock_client.responses.create.return_value = (
        mock_response
    )

    mock_get_client.return_value = (
        mock_client
    )

    with pytest.raises(
        RuntimeError,
        match="empty report"
    ):

        execute_research(
            "AI automation",
            plan
        )

@patch(
    "src.researcher.get_openai_client"
)
def test_researcher_uses_web_search(
    mock_get_client
):

    plan = create_fake_plan()

    mock_response = MagicMock()
    mock_response.output_text = (
        "Research completed."
    )

    mock_client = MagicMock()

    mock_client.responses.create.return_value = (
        mock_response
    )

    mock_get_client.return_value = (
        mock_client
    )

    execute_research(
        "Research AI automation",
        plan
    )

    call_kwargs = (
        mock_client
        .responses
        .create
        .call_args
        .kwargs
    )

    assert call_kwargs["tools"] == [
        {
            "type": "web_search"
        }
    ]