from src.agent import research_agent


def main():

    print("\nAI Research Agent")
    print("=================")

    topic = input(
        "\nWhat would you like me to research? "
    )

    try:

        result = research_agent(
            topic
        )

        plan = result["plan"]

        print("\n=============================")
        print("RESEARCH OBJECTIVE")
        print("=============================")

        print(plan.objective)

        print("\n=============================")
        print("RESEARCH PLAN")
        print("=============================")

        for index, step in enumerate(
            plan.steps,
            start=1
        ):
            print(
                f"{index}. {step}"
            )

        print("\n=============================")
        print("FINAL RESEARCH REPORT")
        print("=============================")

        print(
            result["report"]
        )

    except Exception as error:

        print("\nResearch failed:")
        print(error)


if __name__ == "__main__":
    main()