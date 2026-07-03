<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:6366F1,50:8B5CF6,100:EC4899&height=200&section=header&text=Autonomous%20Research%20Agent&fontSize=42&fontColor=FFFFFF&animation=fadeIn&fontAlignY=38&desc=Plans.%20Searches.%20Scrapes.%20Writes.%20All%20on%20its%20own.&descAlignY=58&descSize=18"/>

<p>
  <img src="https://img.shields.io/badge/status-active-8B5CF6?style=for-the-badge&labelColor=1E1B2E" alt="status"/>
  <img src="https://img.shields.io/badge/license-MIT-6366F1?style=for-the-badge&labelColor=1E1B2E" alt="license"/>
  <img src="https://img.shields.io/badge/python-3.9+-EC4899?style=for-the-badge&labelColor=1E1B2E" alt="python"/>
</p>

<p>
  <a href="https://research-agent-python.streamlit.app/"><strong>Live Demo</strong></a> ·
  <a href="#getting-started"><strong>Getting Started</strong></a> ·
  <a href="#how-it-works"><strong>How It Works</strong></a> ·
  <a href="#screenshots"><strong>Screenshots</strong></a> ·
  <a href="#connect"><strong>Connect</strong></a>
</p>

</div>

<br/>

## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Roadmap](#roadmap)
- [License](#license)
- [Connect](#connect)

<br/>

## Overview

**Autonomous Research Agent** turns a single, plain-English research goal into a fully-researched, structured report. Rather than answering from memory, the agent plans its own multi-step investigation, calls tools to search the web and scrape pages for ground-truth detail, and compiles its findings into a clean Markdown report — with its entire reasoning process visible in real time through a Streamlit interface.

> *"Analyze cybersecurity risks in cloud-based education platforms and propose mitigation strategies."*
> Give it a prompt like that, and it plans, researches, and writes the report on its own.

<br/>

<img width="100%" height="4" src="https://capsule-render.vercel.app/api?type=rect&color=0:6366F1,50:8B5CF6,100:EC4899&height=4"/>

## Problem Statement

Manual research is slow, repetitive, and hard to scale:

- Formulating the right search queries takes iteration and expertise
- Relevant information is scattered across dozens of tabs and sources
- More time goes into copy-pasting and skimming than actual analysis
- Turning scattered notes into one coherent, well-structured report is a separate task in itself
- The entire process has to be repeated from scratch for every new topic

For students, developers, analysts, and lifelong learners, this makes fast, thorough research disproportionately time-consuming.

<br/>

## Solution

Autonomous Research Agent automates the research pipeline end-to-end:

| Problem | How the agent solves it |
|---|---|
| Manual query planning | Breaks a single goal into the right sub-questions automatically |
| Scattered, shallow sources | Uses `web_search` + `scrape_page` to gather ground-truth content, not just snippets |
| No visibility into the process | Streams live agent reasoning so you see exactly what it searched and why |
| Disorganized notes | Synthesizes findings into a structured report — key findings, risks, recommendations, conclusion |
| No reusable output | Exports the final report as a downloadable Markdown file |

In short: you provide the question, the agent handles the investigation.

<br/>

<img width="100%" height="4" src="https://capsule-render.vercel.app/api?type=rect&color=0:6366F1,50:8B5CF6,100:EC4899&height=4"/>

## Features

<table>
<tr>
<td width="50%" valign="top">

**Goal-driven autonomy**
Give it one research goal — it plans and executes the rest.

**Live agent reasoning**
Every tool call is visible in the UI as it happens.

**Structured final reports**
Organized into clear, headed sections automatically.

</td>
<td width="50%" valign="top">

**Configurable depth**
A `Max Iterations` control decides how deep the agent digs.

**One-click export**
Download any report instantly as a `.md` file.

**Session history**
Revisit and compare past research runs.

</td>
</tr>
</table>

<br/>

## Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-6366F1?style=for-the-badge&logo=python&logoColor=white&labelColor=1E1B2E" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-8B5CF6?style=for-the-badge&logo=streamlit&logoColor=white&labelColor=1E1B2E" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/LangChain-A855F7?style=for-the-badge&logo=langchain&logoColor=white&labelColor=1E1B2E" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Groq-EC4899?style=for-the-badge&logoColor=white&labelColor=1E1B2E" alt="Groq"/>
  <img src="https://img.shields.io/badge/python--dotenv-C026D3?style=for-the-badge&logo=.env&logoColor=white&labelColor=1E1B2E" alt="dotenv"/>
  <img src="https://img.shields.io/badge/Markdown-7C3AED?style=for-the-badge&logo=markdown&logoColor=white&labelColor=1E1B2E" alt="Markdown"/>
</p>

<div align="center">

| Layer | Technology | Purpose |
|---|---|---|
| Reasoning / LLM | **Groq** | LPU-accelerated inference powering the agent's decisions |
| Orchestration | **LangChain** | Agent planning, tool routing, and execution loop |
| Interface | **Streamlit** | Interactive UI and live reasoning display |
| Research Tools | Web search & scraping utilities | Ground-truth data gathering |
| Output | Markdown | Structured, portable, exportable reports |
| Language | **Python 3.9+** | Core implementation |

</div>

<br/>

<img width="100%" height="4" src="https://capsule-render.vercel.app/api?type=rect&color=0:6366F1,50:8B5CF6,100:EC4899&height=4"/>

## How It Works

```mermaid
flowchart LR
    A[Research Goal] --> B[Agent Plans Steps]
    B --> C[web_search]
    B --> D[scrape_page]
    C --> E[Synthesize Findings]
    D --> E
    E --> F[Structured Report]
    F --> G[Download .md]

    style A fill:#6366F1,stroke:#1E1B2E,color:#fff
    style B fill:#8B5CF6,stroke:#1E1B2E,color:#fff
    style C fill:#A855F7,stroke:#1E1B2E,color:#fff
    style D fill:#A855F7,stroke:#1E1B2E,color:#fff
    style E fill:#C026D3,stroke:#1E1B2E,color:#fff
    style F fill:#DB2777,stroke:#1E1B2E,color:#fff
    style G fill:#EC4899,stroke:#1E1B2E,color:#fff
```

1. **Enter a research goal** describing what you want investigated.
2. **Run the agent** — it plans its own approach with no further input needed.
3. **Watch it work** — every `web_search` and `scrape_page` call streams live under *Agent Reasoning*.
4. **Review the report** — a structured, headed Markdown document is generated automatically.
5. **Export or revisit** — download the report as `.md`, or browse past runs from the session history.

<br/>

## Getting Started

### Prerequisites

- Python 3.9+
- A [Groq API key](https://console.groq.com/) (powers the agent's reasoning)
- API access for the web search / scraping tool used by the agent

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Amruta-Dabholkar/research-agent-python.git
cd research-agent-python

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment variables
cp .env.example .env   # then fill in your keys
```

`.env`
```env
GROQ_API_KEY=your_groq_api_key_here
# add any additional keys required by the web_search / scrape_page tools
```

### Run

```bash
streamlit run streamlit_app.py
```

Then open the local URL Streamlit provides — typically `http://localhost:8501`.

<br/>

## Project Structure

```
research-agent-python/
├── streamlit_app.py      # Streamlit UI entry point
├── agent/                # Agent logic, tools & orchestration
├── requirements.txt      # Python dependencies
├── .env.example           # Environment variable template
└── README.md
```

<br/>

<img width="100%" height="4" src="https://capsule-render.vercel.app/api?type=rect&color=0:6366F1,50:8B5CF6,100:EC4899&height=4"/>

## Screenshots

<div align="center">

**Live agent reasoning and tool calls**

<img src="https://raw.githubusercontent.com/Amruta-Dabholkar/research-agent-python/main/screenshots/agentic-workflow.png" width="85%"/>

<br/><br/>

**Structured final report**

<img src="https://raw.githubusercontent.com/Amruta-Dabholkar/research-agent-python/main/screenshots/structured-output.png" width="85%"/>

<br/><br/>

**Recommendations, conclusion & export**

<img src="https://raw.githubusercontent.com/Amruta-Dabholkar/research-agent-python/main/screenshots/report-export.png" width="85%"/>

</div>

<br/>

## Roadmap

- [ ] Support for additional LLM providers
- [ ] PDF export alongside Markdown
- [ ] Source citation tracking within reports
- [ ] Multi-agent collaboration for larger research goals

<br/>

## License

Distributed under the **MIT License**. See [`LICENSE`](./LICENSE) for details.

Copyright © 2026 Amruta Anand Dabholkar

<br/>

<div align="center" id="connect">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:EC4899,50:8B5CF6,100:6366F1&height=140&section=header&text=Let's%20Connect&fontSize=30&fontColor=FFFFFF&fontAlignY=45"/>

<p>
  <a href="https://github.com/Amruta-Dabholkar/">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=1E1B2E" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/amruta-dabholkar/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=1E1B2E" alt="LinkedIn"/>
  </a>
</p>

If this project was useful or interesting, consider giving it a star.

</div>
