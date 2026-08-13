from pydantic import BaseModel, Field


class ResearchPlan(BaseModel):
    """
    Structured research plan produced by the planner.
    """

    objective: str = Field(
        description="The main research objective."
    )

    steps: list[str] = Field(
        description=(
            "A concise ordered list of research steps "
            "that can be executed online."
        ),
        min_length=1,
        max_length=5
    )