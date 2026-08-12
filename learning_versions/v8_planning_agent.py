import os
from dotenv import load_dotenv
from openai import OpenAI

# ==========================================
# ENVIRONMENT SETUP
# ==========================================

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# ==========================================
# RESEARCH PLANNER
# ==========================================

def create_research_plan(topic):

    print("\n=================================")
    print("CREATING RESEARCH PLAN")
    print("=================================")

    response = client.responses.create(

        model="gpt-5-mini",

        instructions="""
You are the planning component of an AI research agent.

Your job is to create a short research plan that THIS AI agent
can execute immediately in the current run using web search.

Do NOT:
- suggest interviews
- suggest surveys
- suggest phone calls
- suggest field research
- suggest multi-day or multi-week work
- estimate human project timelines
- create consulting-style deliverables
- suggest future offline research

Create:
- 1-2 steps for simple factual questions
- 3-5 steps for complex research questions

Each step must describe a specific question or topic that can
be researched online right now.

Do not perform the research yet.

Return only a numbered list of research steps.
""",

        input=topic
    )

    plan = response.output_text

    print(plan)

    return plan


# ==========================================
# RESEARCH EXECUTOR
# ==========================================

def execute_research(topic, plan):

    print("\n=================================")
    print("EXECUTING RESEARCH")
    print("=================================")

    research_input = f"""
Research Request:

{topic}


Research Plan:

{plan}


Execute the existing research plan now.

Do not create another research plan.

Use web search to gather current and reliable evidence
for each research step.

Research the topic during this run.

Do not suggest:
- interviews
- surveys
- future work
- multi-week projects
- offline research

Once sufficient information has been collected,
produce the final research report.
"""

    response = client.responses.create(

        model="gpt-5-mini",

        instructions="""
You are the execution component of an AI research agent.

A research plan has already been created.

Your job is NOT to create another plan.

Execute the existing research plan now.

Use web search when current or external information is needed.

Prefer reliable sources such as:
- government websites
- official company sources
- research organizations
- academic sources
- respected industry publications

Avoid unnecessary or repetitive searches.

If different sources disagree, mention the disagreement.

Do not invent statistics.

Do not claim information that cannot be supported
by the research.

When you have enough reliable information,
produce a structured final report containing:

1. Executive Summary
2. Key Findings
3. Opportunity Analysis
4. Business Model Analysis
5. Risks and Adoption Barriers
6. Recommendations
7. Sources

Keep the report useful and concise.
""",

        input=research_input,

        tools=[
            {
                "type": "web_search"
            }
        ]
    )

    # Helpful while learning/debugging
    print("\n=================================")
    print("MODEL ACTIVITY")
    print("=================================")

    for item in response.output:
        print(f"Output type: {item.type}")

    return response.output_text


# ==========================================
# MAIN RESEARCH AGENT
# ==========================================

def research_agent(topic):

    print("\n=================================")
    print("RESEARCH REQUEST")
    print("=================================")

    print(topic)

    # Step 1: Create the research plan
    plan = create_research_plan(topic)

    # Step 2: Execute the plan
    report = execute_research(
        topic,
        plan
    )

    # Step 3: Display final result
    print("\n=================================")
    print("FINAL RESEARCH REPORT")
    print("=================================")

    if report:
        print(report)

    else:
        print(
            "The agent completed the request, "
            "but no final text response was returned."
        )


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":

    topic = input(
        "\nWhat would you like me to research? "
    )

    research_agent(topic)