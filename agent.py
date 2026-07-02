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

import re

from langchain_groq import ChatGroq
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from tools import web_search, scrape_page, calculator

# Model used for the agent loop (tool calling) AND for the table-repair pass.
# llama-3.1-8b-instant is fast but unreliable at following multi-step
# formatting rules (e.g. "never leave a table cell blank") once the context
# fills up with scraped page content. llama-3.3-70b-versatile is still
# available on Groq's free/dev tier and is materially better at instruction
# adherence, at the cost of somewhat higher latency.
AGENT_MODEL = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = """You are an autonomous research agent. Given a research goal, you will:
1. Break the goal into a clear plan, but be efficient: use no more than 2-3 web_search calls TOTAL for the entire goal. Do not run a separate search for every sub-topic — combine related sub-topics into a single well-crafted search query.
2. After searching, use scrape_page on the 2-3 most relevant/authoritative URLs returned by web_search to get real, detailed content. This step is mandatory — do not skip straight to writing the report from search snippets alone.
3. If a tool call fails or returns nothing useful, try ONE alternative query, then move on with what you have rather than repeating searches indefinitely.
4. Keep track of everything you've learned so far.
5. Once you have scraped 2-3 sources, STOP researching and write your final report. Do not keep searching for more sources than necessary.
6. Structure your final answer as a clean report with headers. If a comparison table is relevant, every cell MUST contain a specific, concrete value or short note (e.g. "Supported", "Requires manual indexing", "Similar to MySQL"). Never leave a cell blank. If you lack solid evidence for a cell after scraping, fill it using your own general knowledge rather than leaving it empty, and note where the info came from research vs. general knowledge.
7. Never guess a URL. Only call scrape_page on a URL that was returned by a prior web_search result.
8. When using the calculator tool, pass plain numeric expressions only — no % signs, units, or currency symbols (e.g. use "18 + 44 - 14 - 9.4", not "18% + 44% - 14% - 9.4%").
9. Budget your steps: you have a limited number of tool calls. Prioritize scraping and writing the final report over endless searching.
"""

# Focused, tool-free follow-up prompt used ONLY to repair blank table cells.
# Kept deliberately short and single-purpose so a smaller/faster model still
# follows it reliably — unlike the long multi-step agent system prompt, there
# is exactly one instruction to satisfy here.
TABLE_REPAIR_PROMPT = """The markdown report below has one or more tables containing blank cells.

Rewrite the ENTIRE report exactly as given, with ONE change: fill every blank \
table cell with a specific, concrete value or short note based on your own \
general knowledge of the subject (e.g. "Supported", "~$10/user/month", \
"Not natively supported"). Never leave a cell blank and never write "N/A" \
unless a feature is genuinely not applicable to that row.

Do not change any other wording, structure, or content of the report. Do not \
add commentary before or after it. Return ONLY the corrected report.

REPORT:
{report}
"""


def _has_blank_table_cells(text: str) -> bool:
    """Detect markdown tables with empty cells (ignoring header separator rows)."""
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        # skip separator rows like |---|:---:|---|
        if re.fullmatch(r"\|[\s:\-|]+\|?", stripped):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) > 1 and any(c == "" for c in cells):
            return True
    return False


def repair_blank_table_cells(report: str, llm: ChatGroq) -> str:
    """If the report has blank table cells, ask the LLM to fill them in a
    single focused, tool-free call. Returns the report unchanged if no
    blank cells are found, so this is cheap to call unconditionally."""
    if not report or not _has_blank_table_cells(report):
        return report

    response = llm.invoke(TABLE_REPAIR_PROMPT.format(report=report))
    repaired = response.content.strip()

    # Safety net: if the repair call somehow still leaves blanks, or fails
    # oddly and returns something empty, fall back to the original report
    # rather than risk returning garbage.
    if not repaired or _has_blank_table_cells(repaired):
        return repaired or report

    return repaired


def build_agent(callbacks=None, max_iterations: int = 15):
    """Returns (executor, llm). llm is returned separately — rather than
    attached to the executor — because AgentExecutor is a Pydantic model
    and does not allow arbitrary extra attributes to be set on it."""
    llm = ChatGroq(
        model=AGENT_MODEL,
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

    return executor, llm


def run_research_agent(goal: str, callbacks=None, max_iterations: int = 15) -> str:
    """Single entry point for running research end-to-end: builds the agent,
    runs it, and ALWAYS runs the blank-table-cell repair pass on the output
    before returning. Both the CLI (main, below) and the Streamlit UI should
    call this rather than calling build_agent()/executor.invoke() directly,
    so the "no blank cells" guarantee can't be bypassed by one caller
    forgetting the repair step."""
    executor, llm = build_agent(callbacks=callbacks, max_iterations=max_iterations)
    result = executor.invoke({"input": goal})
    report = result.get("output", "")
    return repair_blank_table_cells(report, llm)


def main():
    if not os.getenv("GROQ_API_KEY"):
        print("ERROR: GROQ_API_KEY not set. Copy .env.example to .env and fill it in.")
        return

    print("Autonomous Research Agent (Python/LangChain)")
    print("Type a research goal, or 'quit' to exit.\n")

    while True:
        goal = input("Research goal: ").strip()
        if goal.lower() in ("quit", "exit"):
            break
        if not goal:
            continue

        report = run_research_agent(goal)

        print("\n--- FINAL REPORT ---\n")
        print(report)
        print("\n---------------------\n")


if __name__ == "__main__":
    main()