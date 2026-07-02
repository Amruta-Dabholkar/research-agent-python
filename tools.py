"""
Tools available to the research agent.

Each tool is a plain Python function decorated with @tool from LangChain.
The docstring IS the tool description the LLM reads to decide when to use it —
keep it precise, since a vague docstring leads to the agent misusing the tool.
"""

import os
import re
import requests
from bs4 import BeautifulSoup
from langchain.tools import tool

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")


@tool
def web_search(query: str) -> str:
    """Searches Google via SerpAPI for the given query and returns the top
    results as title/link/snippet text. Use this first to find information
    or candidate URLs before deciding whether to scrape a full page."""
    serpapi_key = os.getenv("SERPAPI_API_KEY")
    if not serpapi_key:
        return "Error: SERPAPI_API_KEY is not set in the environment."

    params = {"q": query, "api_key": serpapi_key, "engine": "google"}
    try:
        resp = requests.get("https://serpapi.com/search", params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return f"Search failed: {e}"

    results = []
    for item in data.get("organic_results", [])[:5]:
        title = item.get("title", "")
        link = item.get("link", "")
        snippet = item.get("snippet", "")
        results.append(f"- {title}\n  {link}\n  {snippet}")

    if not results:
        return "No results found for that query."
    return "\n".join(results)



@tool
def scrape_page(url: str) -> str:
    """Fetches a webpage and returns its main readable text content with HTML
    tags stripped, truncated to ~3000 characters. Use sparingly — only when a
    search snippet doesn't already answer the question. If this returns
    empty or an error, do not retry the same URL; use a different source."""
    try:
        resp = requests.get(
            url,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0 (compatible; ResearchAgent/1.0)"},
        )
        resp.raise_for_status()
    except Exception as e:
        return f"Failed to fetch page: {e}"

    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "noscript"]):
        tag.decompose()

    text = " ".join(soup.get_text(separator=" ").split())
    if not text:
        return "Page returned no extractable text content."
    return text[:3000]


@tool
def calculator(expression: str) -> str:
    """Evaluates a basic arithmetic expression, e.g. '19*12 - 24.99*12' or
    '(50-40)/50*100'. Use this for comparing prices, totals, or percentages
    rather than doing math yourself."""
    if not re.fullmatch(r"[0-9+\-*/(). %]+", expression):
        return "Error: expression contains disallowed characters."
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Calculation error: {e}"
