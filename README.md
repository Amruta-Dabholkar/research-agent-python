# 🔍 Autonomous Research Agent

An autonomous research agent that takes a broad research goal, plans its own steps, searches the web, scrapes pages for ground-truth detail, and compiles a structured report — all with minimal human input.

**Powered by:** Groq · Streamlit · LangChain

🔗 **Live demo:** [research-agent-python.streamlit.app](https://research-agent-python.streamlit.app/)
👤 **Author:** [Amruta Dabholkar](https://github.com/Amruta-Dabholkar) · [LinkedIn](https://www.linkedin.com/in/amruta-dabholkar/)

---

## ✨ Features

- **Goal-driven autonomy** — Give it a single research goal in plain English and the agent breaks it down into sub-tasks on its own.
- **Live agent reasoning** — Watch each tool call as it happens (`web_search`, `scrape_page`, etc.) along with the exact query or URL used.
- **Structured final report** — Automatically compiled into clear sections (e.g. Introduction, Key Risks, Mitigation Strategies, Conclusion) with numbered, bolded key points.
- **Configurable iteration limit** — A `Max Iterations` slider controls how many reasoning/tool-use steps the agent is allowed to take (default: 10).
- **Exportable reports** — Download any completed report as a Markdown (`.md`) file.
- **Session history** — Past runs are saved and viewable within the current session for easy comparison.

---

## 🖥️ How It Works

1. Enter a **Research goal** describing what you want investigated (e.g. *"Analyze cybersecurity risks in cloud-based education platforms and propose mitigation strategies."*).
2. Click **Run research**.
3. The agent plans its approach and works through it autonomously, shown live under **Agent reasoning**:
   - `web_search` — queries the web for relevant sources.
   - `scrape_page` — pulls detailed, ground-truth content from specific pages.
4. Once complete, a **Final report** is generated with headed sections and takeaways.
5. Use **Download report (.md)** to save the report locally, or expand **Past runs in this session** to revisit earlier reports.

---

## ⚙️ Requirements

- Python 3.9+
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- A **Groq API key** (the agent's reasoning is Groq-powered)
- A web search / scraping API key or service, depending on how `web_search` and `scrape_page` are implemented in this project

> ⚠️ The app will display an **"API keys required"** status until valid keys are configured.

---

## 🔑 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Amruta-Dabholkar/research-agent-python.git
   cd research-agent-python
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your API keys, e.g. via a `.env` file or Streamlit secrets:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   # add any additional keys required for web_search / scrape_page tools
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Open the local URL Streamlit provides (usually `http://localhost:8501`) in your browser.

---

## 💡 Tips for Best Results

- **Break down large goals** into smaller, focused sub-tasks for better results.
- **Use consistent keywords** in your research goal to improve search accuracy.
- **Save and review past reports** to refine future research prompts.
- **Be patient** — complex research tasks may take the agent a few minutes to complete.

---

## 📦 Output Format

Reports are compiled in structured Markdown, typically including:

- **Introduction** — framing of the research topic
- **Core Findings** — numbered, bolded points with explanations
- **Recommendations / Mitigation Strategies** — actionable next steps
- **Conclusion** — summary tying findings back to the original goal

---

## ❤️ Credits

Made with Streamlit + LangChain.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — see the LICENSE file for details.

Copyright (c) 2026 Amruta Anand Dabholkar
