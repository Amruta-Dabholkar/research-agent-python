"""
Autonomous Research & Reporting Agent — Python/LangChain version.

This is the "no abstraction" rebuild of the n8n prototype: instead of n8n's
built-in AI Agent node hiding the reasoning loop, this file wires up the
ReAct loop explicitly using LangChain primitives, so every piece
(model, tools, memory, iteration limit) is visible and tunable in code.
"""

import os
from dotenv import load_dotenv

load_dotenv()  # ← move this up, before importing tools (or anything that reads env vars at import time)

from langchain_groq import ChatGroq
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from tools import web_search, scrape_page, calculator

SYSTEM_PROMPT = """You are an autonomous research agent. Given a research goal, you will:
1. Break the goal into a clear multi-step plan
2. Use the available tools to gather real information — never fabricate data
3. If a tool call fails or returns nothing useful, try a different query or approach before giving up
4. Keep track of everything you've learned so far
5. Only give a final answer once you have enough evidence to fully address the goal
6. Structure your final answer as a clean report with headers and, where relevant, a comparison table
7. Never guess a URL. Only call scrape_page on a URL that was returned by a prior web_search result.
8. When using the calculator tool, pass plain numeric expressions only — no % signs, units, or currency symbols (e.g. use "18 + 44 - 14 - 9.4", not "18% + 44% - 14% - 9.4%").
"""


def build_agent(callbacks=None, max_iterations: int = 10) -> AgentExecutor:
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        model_kwargs={"parallel_tool_calls": False},
    )
    tools = [web_search, scrape_page, calculator]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            MessagesPlaceholder("chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        ]
    )

    agent = create_tool_calling_agent(llm, tools, prompt)

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # max_iterations is the safety guard against infinite loops — same
    # purpose as the "max iteration limit" set in the n8n AI Agent node.
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,  # prints the live Thought -> Action -> Observation trace
        max_iterations=max_iterations,
        handle_parsing_errors=True,
        max_execution_time=120,
        callbacks=callbacks,
    )
    return executor


def main():
    if not os.getenv("GROQ_API_KEY"):
        print("ERROR: GROQ_API_KEY not set. Copy .env.example to .env and fill it in.")
        return

    executor = build_agent()
    print("Autonomous Research Agent (Python/LangChain)")
    print("Type a research goal, or 'quit' to exit.\n")

    while True:
        goal = input("Research goal: ").strip()
        if goal.lower() in ("quit", "exit"):
            break
        if not goal:
            continue

        result = executor.invoke({"input": goal})

        print("\n--- FINAL REPORT ---\n")
        print(result["output"])
        print("\n---------------------\n")


if __name__ == "__main__":
    main()