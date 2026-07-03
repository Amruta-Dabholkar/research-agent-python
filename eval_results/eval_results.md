# Evaluation Results

Test set: 18 research queries spanning factual, comparative, and ambiguous/open-ended categories. Full per-query transcripts and raw tool-call traces are in `eval_results/raw/`.

## Headline numbers

- **Completed 16/18 queries** (89%) without hitting the iteration limit or erroring out
- **Average latency:** 58.9s per report (min 11.5s, max 99.4s)
- **Average distinct sources per report:** 7.9
- **Average tool calls per query:** 2.5
- **Tool-level errors encountered:** 1 across all runs (0.1 per query on average) — all recovered from automatically without crashing the run
- **Avg "answered the question" score (manual, 1-5):** 3.9
- **Avg factual accuracy score (manual, 1-5):** 3.3

## By category

- **Ambiguous**: 6/6 completed
- **Comparative**: 5/7 completed
- **Factual**: 5/5 completed

## Per-query results

| # | Category | Goal | Completed | Latency (s) | Sources | Tool calls | Errors | Answered (1-5) | Accuracy (1-5) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | factual | What is the current stable version of Python? | True | 12.8 | 10 | 3 | 0 | 1 | 2 |
| 2 | factual | Who is the current CEO of OpenAI? | True | 74.4 | 13 | 3 | 0 | 5 | 1 |
| 3 | factual | What is the population of Japan as of the most recent est... | True | 22.4 | 5 | 2 | 0 | 5 | 5 |
| 4 | factual | What year was the first iPhone released? | True | 41.7 | 5 | 2 | 0 | 5 | 5 |
| 5 | factual | What is the boiling point of water at sea level in Celsius? | True | 14.0 | 5 | 2 | 0 | 5 | 5 |
| 6 | comparative | Compare AWS, Azure, and GCP pricing for a small startup's... | False | 11.5 | 0 | 0 | 0 | 1 | 1 |
| 7 | comparative | Compare React and Vue for building an admin dashboard. | True | 79.5 | 10 | 3 | 0 | 3 | 2 |
| 8 | comparative | Compare the top 5 SQL query optimization techniques acros... | False | 93.1 | 20 | 4 | 0 | 1 | 2 |
| 9 | comparative | Compare Python and JavaScript for backend web development. | True | 48.0 | 5 | 2 | 0 | 5 | 5 |
| 10 | comparative | Compare the Tesla Model 3 and Model Y in terms of price a... | True | 99.4 | 8 | 3 | 0 | 5 | 3 |
| 11 | comparative | Compare the pros and cons of remote work versus in-office... | True | 51.8 | 5 | 2 | 0 | 5 | 4 |
| 12 | comparative | Compare Notion and Obsidian for personal knowledge manage... | True | 62.5 | 5 | 2 | 0 | 5 | 5 |
| 13 | ambiguous | Research the best programming language to learn in 2026. | True | 78.9 | 10 | 3 | 1 | 3 | 2 |
| 14 | ambiguous | Research the current state of AI safety efforts. | True | 75.6 | 14 | 3 | 0 | 3 | 2 |
| 15 | ambiguous | Which is better, iOS or Android? | True | 62.0 | 5 | 2 | 0 | 5 | 5 |
| 16 | ambiguous | Research the future of remote work. | True | 77.0 | 10 | 3 | 0 | 3 | 2 |
| 17 | ambiguous | Evaluate whether remote learning is effective. | True | 57.8 | 5 | 2 | 0 | 5 | 5 |
| 18 | ambiguous | Research renewable energy adoption trends in rural India. | True | 97.6 | 8 | 4 | 0 | 5 | 3 |