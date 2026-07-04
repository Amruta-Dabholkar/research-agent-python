# Query 04 (factual)

**Goal:** What year was the first iPhone released?

**Latency:** 41.7s  
**Completed:** True  
**Tool calls:** 2 (search=1, scrape=0, calc=1)  
**Distinct source URLs:** 5  
**Tool-level errors encountered:** 0  

---

## Final report

The first iPhone was released in the year 2007.

---

## Tool call trace

### Tool call: `web_search`
**Input:** `{'query': 'first iPhone release year'}`

**Observation:**
```
- iPhone - Wikipedia
  https://en.wikipedia.org/wiki/IPhone
  The first-generation iPhone was announced by then–Apple CEO and co-founder Steve Jobs on January 9, 2007, at Macworld 2007, and launched later that year. Since then, Apple has annually released new iPhone models and iOS versions; the latest models are the iPhone 17, the...
- The History of Every iPhone Model from 2007–2026
  https://www.iphonelife.com/content/evolution-iphone-every-model-2007-2016
  When did the first iPhone come out? We have the full history of the iPhone, from the first iPhone to the iPhone 17. This article will cover the evolution of iPhones over the years and discuss the notable changes made with each release.
- Today in History: June 29, Apple releases the first iPhone... | wfmz.com
  https://www.wfmz.com/news/ap/ap-this-day-in-history/today-in-history-june-29-apple-releases-the-first-iphone-to-consumers/article_b932d686-9c49-5a3d-8554-3ce1f970cff7.html
  Today's highlight in history: On June 29, 2007, the first version of the iPhone went on sale to the public; over 2.3 billion iPhones have been sold to date.
- History of Apple iPhones. See how much the iPhone has... | Medium
  https://medium.com/macoclock/history-of-apple-iphones-57c06323135b
  The iPhone XS Max introduced the option of a larger model of the iPhone X one year after the 10-year anniversary model, with all the same enhancements as the iPhone XS, but in a larger, expensive, and fabulous package. Apple iPhone 11 (2019).
- iOS Ver
```

### Tool call: `calculator`
**Input:** `{'expression': '2007'}`

**Observation:**
```
2007
```


---

## Manual scoring (fill in after reading the report above)

- **Answered the question (1-5):** 
- **Factual accuracy (1-5):** 
- **Notes:** 


---

## LLM-judge scoring (automated, not human-reviewed)

- **Answered the question (1-5):** 5
- **Factual accuracy (1-5):** 5
- **Judge notes:** The report accurately and completely answers the goal with evidence from the tool call trace.
