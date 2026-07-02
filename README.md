# Autonomous Research & Reporting Agent — Python/LangChain Version

This is the raw-code rebuild of the original n8n prototype. Same ReAct
(Reason → Act → Observe) pattern, same three tools, but the reasoning loop,
memory, and iteration limit are now explicit in code instead of hidden
inside a no-code node.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy the env file and add your keys:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and paste in your `OPENAI_API_KEY` (platform.openai.com)
   and `SERPAPI_API_KEY` (serpapi.com).

4. Run it:
   ```bash
   python agent.py
   ```

5. Type a research goal at the prompt, e.g.:
   ```
   Research the top 3 project management tools and compare their pricing tiers.
   ```

With `verbose=True` set in `agent.py`, you'll see the live Thought → Action →
Observation trace print to the terminal as it runs — this is your ReAct loop
happening in real time, the same thing the n8n Logs panel showed you.

## Architecture

```
tools.py    -> web_search, scrape_page, calculator (the tool layer)
agent.py    -> builds the LLM, binds the tools, adds memory,
               wraps it all in an AgentExecutor with max_iterations=10
```

- **web_search**: calls SerpAPI directly via `requests`, returns top 5 results
- **scrape_page**: fetches a URL, strips HTML with BeautifulSoup, truncates to
  ~3000 chars (this is the fix for the context-overflow bug you hit in n8n —
  here it's a hard limit in code instead of a UI toggle)
- **calculator**: safely evaluates arithmetic expressions for price/percentage comparisons
- **memory**: `ConversationBufferMemory` keeps the conversation across turns
  within one run of the script
- **max_iterations**: the safety guard against infinite loops, same concept
  as n8n's iteration limit setting

## How this differs from the n8n version (for your resume/interview)

| n8n version | Python version |
|---|---|
| AI Agent node hides the loop internals | Loop is explicit via `AgentExecutor` |
| Tool config via UI forms | Tools are plain Python functions with docstrings |
| Memory via Simple Memory node | `ConversationBufferMemory` object in code |
| Iteration limit via node setting | `max_iterations=10` parameter |
| Delivery via Slack node | Add your own delivery step (see below) |

## Next steps to extend

- **Slack delivery**: use the `slack_sdk` package to post `result["output"]`
  to a channel via a bot token or incoming webhook.
- **Persistent memory**: swap `ConversationBufferMemory` for a vector-store-
  backed memory (e.g. Chroma, FAISS) to recall past research across separate
  runs, not just within one session.
- **Critic step**: add a second LLM call that reviews the final report for
  accuracy/completeness before returning it to the user.
- **Cost tracking**: LangChain exposes token usage via callbacks — log this
  per run if you want usage/cost tracking like the original doc mentions.
