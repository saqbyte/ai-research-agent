import pytest
from pydantic import ValidationError

from src.models import ResearchPlan


def test_research_plan_creation():

    plan = ResearchPlan(
        objective="Research AI automation.",
        steps=[
            "Research the market.",
            "Identify opportunities."
        ]
    )

    assert plan.objective == (
        "Research AI automation."
    )

    assert len(plan.steps) == 2


def test_research_plan_requires_steps():

    with pytest.raises(ValidationError):

        ResearchPlan(
            objective="Research AI automation.",
            steps=[]
        )


def test_research_plan_maximum_five_steps():

    with pytest.raises(ValidationError):

        ResearchPlan(
            objective="Research AI automation.",
            steps=[
                "Step 1",
                "Step 2",
                "Step 3",
                "Step 4",
                "Step 5",
                "Step 6"
            ]
        )