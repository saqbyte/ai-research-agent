from src.agent import research_agent


def main():

    print("\nAI Research Agent")
    print("=================")

    topic = input(
        "\nWhat would you like me to research? "
    )

    try:

        result = research_agent(topic)

        print("\n=============================")
        print("RESEARCH PLAN")
        print("=============================")

        print(result["plan"])

        print("\n=============================")
        print("FINAL RESEARCH REPORT")
        print("=============================")

        print(result["report"])

    except Exception as error:

        print("\nResearch failed:")
        print(error)


if __name__ == "__main__":
    main()