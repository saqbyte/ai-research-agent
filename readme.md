AI Research Agent

A learning project where I am building an AI research agent from scratch and progressively improving it from simple rule-based logic to an LLM-powered agent with tool calling and web search.

This project is part of my hands-on journey into AI agents, LLMs, Python, and AI automation.

🚀 Project Goal

The goal of this project is to understand how AI agents are actually built rather than only using existing agent frameworks.

I am developing the agent step by step, documenting each stage and learning how different components work together.

🧠 Learning Journey

The project currently contains the following stages:

Version	What I Learned
V1	Rule-based research logic
V2	First interaction with an LLM
V3	LLM-based decision making
V4	Tool definitions and function calling
V5	Building an agent/tool execution loop
V6	Adding web search capabilities

The project will continue to evolve as I learn more about AI agents.

🏗️ Current Architecture

The current agent follows this general workflow:

User
  │
  ▼
Research Topic
  │
  ▼
LLM
  │
  ├── Need external information?
  │          │
  │          ▼
  │      Search Tool
  │          │
  │          ▼
  │      Search Results
  │          │
  └──────────┘
  │
  ▼
Research Response

The architecture is still under development and will become more advanced as the project progresses.

📁 Project Structure
01-research-agent/
│
├── README.md
├── .env.example
├── .gitignore
├── requirements.txt
├── test_connection.py
│
├── v1_rule_based.py
├── v2_first_llm_call.py
├── v2_llm_decision.py
├── v3_manual_tool.py
├── v4_tool_calling.py
├── v5_agent_loop.py
└── v6_web_search.py

Each version represents a milestone in the development and learning process.

🛠️ Technologies
Python
OpenAI API
python-dotenv
Function Calling / Tools
Git & GitHub
VS Code
⚙️ Setup
1. Clone the repository
git clone <repository-url>
cd 01-research-agent
2. Install dependencies
pip install -r requirements.txt
3. Configure environment variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here

Never commit your actual .env file or API key to GitHub.

4. Run an agent version

For example:

python v6_web_search.py
🔐 Environment Variables

The project uses:

OPENAI_API_KEY

A .env.example file is included to show the required configuration without exposing the actual API key.

📚 What I'm Learning

Through this project, I am learning:

How LLM APIs work
How to structure AI applications in Python
How LLMs make tool decisions
Function/tool calling
Agent execution loops
Connecting external tools to LLMs
Web research workflows
Error handling and debugging
Git and GitHub
Building and documenting AI projects
🔭 What's Next?

Planned improvements include:

Real web search integration
Better research result processing
Source extraction and citations
Structured research reports
Multiple tools
Agent memory
Better error handling
Improved prompts
More autonomous decision making
Eventually exploring agent frameworks such as LangGraph
📈 Project Status

Status: 🚧 In Development

This repository is intentionally being built incrementally. Each version represents something I learned and implemented rather than jumping directly to a finished framework-based agent.

👨‍💻 About This Project

This is a hands-on portfolio project focused on learning AI agent engineering by building from first principles.

The objective is not just to make an agent that works, but to understand why it works, how its components interact, and how the system can be improved over time.