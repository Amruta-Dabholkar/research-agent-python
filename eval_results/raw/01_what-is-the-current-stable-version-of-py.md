# Query 01 (factual)

**Goal:** What is the current stable version of Python?

**Latency:** 12.8s  
**Completed:** True  
**Tool calls:** 3 (search=3, scrape=0, calc=0)  
**Distinct source URLs:** 10  
**Tool-level errors encountered:** 0  

---

## Final report

The current stable version of Python is Python 3.14.0.

---

## Tool call trace

### Tool call: `web_search`
**Input:** `{'query': 'current stable version of Python'}`

**Observation:**
```
- Status of Python versions
  https://devguide.python.org/versions/
  The main branch is currently the future Python 3.16, and is the only branch that accepts new features. The latest release for each Python version ...
- Is Python a stable language? - Python Help - Discussions on
  https://discuss.python.org/t/is-python-a-stable-language/21554
  Python itself, however, is very stable; code written for Python 3.0 (released 2008) will almost certainly run on the current version of Python, and ...
- Python 3.9.6, 3.8.11, 3.7.11, and 3.6.14 are now available -
  https://discuss.python.org/t/python-3-9-6-3-8-11-3-7-11-and-3-6-14-are-now-available/9455
  Python 3.9.6 is the newest major stable release of the Python programming language, and it contains many new features and optimizations.
- Python Release Python 3.9.0a5 | Python.org
  https://www.python.org/downloads/release/python-390a5/
  Alpha releases are intended to make it easier to test the current state of new features and bug fixes and to test the release process.
- stable version – IndicThreads
  https://indicthreads.com/tag/stable-version/
  ... Views 0 Comments Articles , Python , Python Articles , stable version ... The standard documentation for the current stable version of Python is also
```

### Tool call: `web_search`
**Input:** `{'query': 'current stable version of Python'}`

**Observation:**
```
- Status of Python versions
  https://devguide.python.org/versions/
  The main branch is currently the future Python 3.16, and is the only branch that accepts new features. The latest release for each Python version ...
- Is Python a stable language? - Python Help - Discussions on
  https://discuss.python.org/t/is-python-a-stable-language/21554
  Python itself, however, is very stable; code written for Python 3.0 (released 2008) will almost certainly run on the current version of Python, and ...
- Python 3.9.6, 3.8.11, 3.7.11, and 3.6.14 are now available -
  https://discuss.python.org/t/python-3-9-6-3-8-11-3-7-11-and-3-6-14-are-now-available/9455
  Python 3.9.6 is the newest major stable release of the Python programming language, and it contains many new features and optimizations.
- Python Release Python 3.9.0a5 | Python.org
  https://www.python.org/downloads/release/python-390a5/
  Alpha releases are intended to make it easier to test the current state of new features and bug fixes and to test the release process.
- stable version – IndicThreads
  https://indicthreads.com/tag/stable-version/
  ... Views 0 Comments Articles , Python , Python Articles , stable version ... The standard documentation for the current stable version of Python is also
```

### Tool call: `web_search`
**Input:** `{'query': 'latest stable version of Python'}`

**Observation:**
```
- Download Python | Python.org
  https://www.python.org/downloads/
  Looking for Python with a different OS? Python for Windows, Linux/Unix, macOS, Android, iOS, other Want to help test development versions of Python 3.15? Pre-releases, Docker images
- Python Release Python 3.14.0 | Python.org
  https://www.python.org/downloads/release/python-3140/
  This is the stable release of Python 3.14.0 Python 3.14.0 is the newest major release of the Python programming language, and it contains many new features and optimisations compared to Python 3.13.
- Latest Python Version (2025) - What's New in Python 3.14?
  https://www.liquidweb.com/blog/latest-python-version/
  Python continues to evolve, bringing powerful new features, enhanced security, and performance improvements with every release. The latest major version, Python 3.14 was officially released on October 7, 2025. Let's explore the key features of Python's current version, how to download and install it, and what this release means for developers.
- Python Latest Version - Support Lifecycle & EOL
  https://versionlog.com/python/
  Python Lifecycle & End of Life (EOL) Policy Python follows a clear five-year support policy for every minor release. Once a version is fully released, it enters the bugfix phase where the core team accepts both bug fixes and security updates. New installer packages appear roughly every two months during this period to keep the ecosystem stable and reliable. After approximately two years, the ...

```


---

## Manual scoring (fill in after reading the report above)

- **Answered the question (1-5):** 
- **Factual accuracy (1-5):** 
- **Notes:** 


---

## LLM-judge scoring (automated, not human-reviewed)

- **Answered the question (1-5):** 1
- **Factual accuracy (1-5):** 2
- **Judge notes:** The report directly answers the goal, but its claim about the current stable version of Python is partially supported by the evidence, which actually points to Python 3.14.0 as the latest stable release, but also mentions Python 3.9.6 as a major stable release.
