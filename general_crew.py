# -*- coding: utf-8 -*-
import os
from crewai import Agent, Crew, Process, Task, LLM

# 1. LOCAL MODEL CONFIGURATION (Optimized for fast local execution)
local_llm = LLM(
    model="ollama/qwen2.5:1.5b", 
    base_url="http://localhost:11434",
    temperature=0.7
)

# 2. GENERAL PURPOSE AGENTS DEFINITION
director_agent = Agent(
    role="Project Director",
    goal="Analyze the main objective, create a structured execution plan, and oversee the team's output.",
    backstory="An elite manager expert in systemizing complex requests. Breaks down goals into flawless actionable structures.",
    llm=local_llm,
    allow_delegation=True,
    max_iter=3,
    verbose=True
)

expert_agent = Agent(
    role="Technical Specialist",
    goal="Execute the tasks assigned by the Director with maximum precision and depth.",
    backstory="A versatile developer and researcher with deep technical knowledge. Delivers highly optimized results.",
    llm=local_llm,
    allow_delegation=False,
    max_iter=3,
    verbose=True
)

auditor_agent = Agent(
    role="Quality Assurance Auditor",
    goal="Review the Specialist's work, detect flaws, and force iterative corrections until output is perfect.",
    backstory="A meticulous and uncompromising critic. Will reject any work containing errors, gaps, or suboptimal logic.",
    llm=local_llm,
    allow_delegation=False,
    max_iter=3,
    verbose=True
)

# 3. RECURSIVE FEEDBACK TASKS
task_planning = Task(
    description="Analyze the following objective: '{user_objective}'. Design a comprehensive execution framework.",
    expected_output="A structured Markdown plan outlining the requirements, logic, and implementation phases.",
    agent=director_agent
)

task_execution = Task(
    description="Take the Director's blueprint and fully implement or write the core solution requested.",
    expected_output="The complete technical solution or exhaustive documentation depending on the prompt requirements.",
    agent=expert_agent
)

task_audit = Task(
    description=(
        "Thoroughly analyze the output from the previous execution task. Run a complete mental review. "
        "If you find any bugs, logical gaps, or missing requirements, send it back to the Specialist "
        "with explicit feedback for refactoring. Do not conclude until the work meets master-level standards."
    ),
    expected_output="The final, fully optimized, and verified solution alongside a brief audit report.",
    agent=auditor_agent
)

# 4. CREW ORCHESTRATION WITH LOGS ENABLED
general_crew = Crew(
    agents=[director_agent, expert_agent, auditor_agent],
    tasks=[task_planning, task_execution, task_audit],
    process=Process.sequential, 
    verbose=True,
    output_log_file="general_agents_log.txt"
)

if __name__ == "__main__":
    prompt = "Create a scalable architecture blueprint for a secure microservices system using FastAPI and Docker."
    print(f"\n[+] Booting local agents (1.5B) with recursive correction loop...\n")
    final_output = general_crew.kickoff(inputs={"user_objective": prompt})
    print("\n" + "="*50 + "\n[+] FINAL PERFECTED WORK:\n" + "="*50 + "\n")
    print(final_output)

