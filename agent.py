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
1. Break the goal into a clear plan, but be efficient: use no more than 2-3 web_search calls TOTAL for the entire goal. Do not run a separate search for every sub-topic — combine related sub-topics into a single well-crafted search query.
2. After searching, use scrape_page on the 2-3 most relevant/authoritative URLs returned by web_search to get real, detailed content. This step is mandatory — do not skip straight to writing the report from search snippets alone.
3. If a tool call fails or returns nothing useful, try ONE alternative query, then move on with what you have rather than repeating searches indefinitely.
4. Keep track of everything you've learned so far.
5. Once you have scraped 2-3 sources, STOP researching and write your final report. Do not keep searching for more sources than necessary.
6. Structure your final answer as a clean report with headers. If a comparison table is relevant, every cell MUST contain a specific, concrete value or short note (e.g. "Supported", "Requires manual indexing", "Similar to MySQL"). Never leave a cell blank. If you lack solid evidence for a cell after scraping, fill it using your own general SQL knowledge rather than leaving it empty, and note where the info came from research vs. general knowledge.
7. Never guess a URL. Only call scrape_page on a URL that was returned by a prior web_search result.
8. When using the calculator tool, pass plain numeric expressions only — no % signs, units, or currency symbols (e.g. use "18 + 44 - 14 - 9.4", not "18% + 44% - 14% - 9.4%").
9. Budget your steps: you have a limited number of tool calls. Prioritize scraping and writing the final report over endless searching.
"""


def build_agent(callbacks=None, max_iterations: int = 15) -> AgentExecutor:
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
        verbose=True,
        max_iterations=max_iterations,
        handle_parsing_errors=True,
        max_execution_time=180,  # was 120 — scraping takes longer than search
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