# 🤖 Autonomous Local Multi-Agent Workspace

A robust, high-performance **local multi-agent AI system** engineered for accelerated software development, technical research, and complex system automation. This environment runs 100% locally on my PC, leveraging local compute resource optimization and hardware acceleration.

## 🚀 System Architecture
The workspace orchestrates a deterministic pipeline of three specialized autonomous agents operating within an iterative feedback and self-correction loop:

1. **Project Director (Manager):** Analyzes the root user objective, provisions the execution strategy, and builds the modular architecture design.
2. **Technical Specialist (Developer):** Implements raw source code, handles API routing layout, and establishes infrastructure configuration.
3. **Quality Assurance Auditor (Reviewer):** Conducts a strict code-review process, runs mental telemetry evaluation, and forces the Developer into refactoring cycles if logical gaps or vulnerabilities are detected.

## 🛠️ Production Tech Stack
- **Core LLM Inference:** [Ollama](https://ollama.com) (Using lightweight, high-speed `qwen2.5:1.5b` to prevent VRAM bottlenecks)
- **Agent Orchestration Framework:** [CrewAI Engine](https://crewai.com)
- **Compute Runtime Environment:** Python 3.11+ / PyTorch (CUDA 12.4 Enabled) / TensorFlow
- **Telemetry & Logging:** Native JSONL thread tracking through localized stdout and persistent execution logs (`general_agents_log.txt`).

## 📦 Setup & Environment Initialization

Ensure your local virtual environment is isolated to avoid package conflicts across core ML libraries:

```bash
# 1. Initialize repository and activate the local environment
cd C:\Users\danir\Documents\Universidad\4Informatica\IA\workspace_agents
C:\IA\entornos\hackathon_env\Scripts\activate

# 2. Verify framework dependencies
pip install crewai crewai-tools langchain-community
```

## 🖥️ Production Execution

To trigger the localized execution pipeline and run recursive tasks, maintain Ollama running in the background and execute:

```bash
# Run the autonomous multi-agent pipeline
python general_crew.py
```

All agent interactions, cross-evaluations, and finalized architectural mockups will be written in real-time to the terminal interface and appended to `general_agents_log.txt`.
