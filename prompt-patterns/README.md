# Prompt Patterns

A practical guide to reusable prompt structures for consistent, high-quality AI outputs.

## Overview

This project explores how well-designed prompt patterns can replace vague, open-ended requests with structured templates that produce reliable and targeted results. Topics covered include:

- Reusable prompt structures for different tasks
- Instructional, comparative, QA, and data extraction patterns
- Transforming weak prompts into structured, repeatable templates

## Learning Objectives

By the end of this quest, you will be able to:

- Learn key prompt design patterns
- Transform a single use-case into a reusable prompt template
- Improve weak prompts by applying structured patterns

## Requirements

- Python 3.9+
- `numpy`
- `pandas`
- `jupyter`
- OpenAI Playground or ChatGPT interface

## Setup

1. **Clone the repository**
   ```bash
   git clone https://acad.learn2earn.ng/git/jmomoh/prompt-patterns
   cd prompt-patterns
   ```

2. **Verify Python version**
   ```bash
   python --version
   # Expected: Python 3.9+
   ```

3. **Install dependencies**
   ```bash
   pip install numpy pandas jupyter
   ```

## Exercises

### Exercise 0: Environment and Libraries
Set up the Python development environment, verify the installation, and confirm all required libraries are importable.

```python
import sys
print(f"Python version: {sys.version}")

import jupyter, numpy, pandas
print("All libraries imported successfully!")
print(f"Numpy version: {numpy.__version__}")
print(f"Pandas version: {pandas.__version__}")
```

**Result:** Python 3.12.3 confirmed, all libraries loaded successfully.

---

### Exercise 1: Summarization Pattern

A weak prompt was refined into a reusable 3-bullet summarization template and tested on two different topics.

**Weak prompt:** *"Summarize this text."*

**Reusable pattern:** *"Summarize the following text in 3 bullet points, focusing on the main points, key challenges, and future outlook."*

| Test | Topic | Result |
|---|---|---|
| Test 1 | Climate change | 3 bullets: Main Impacts → Scientific Responses → Preparation Strategies |
| Test 2 | Cybersecurity | 3 bullets: Main Points → Key Challenges → Future Outlook |

Both tests produced consistently structured outputs despite being completely different subjects, demonstrating the pattern's reliability across topics.

**Key Takeaway:** Specifying format (3 bullets) and content focus (what to highlight) removes ambiguity and ensures every output follows the same structure, making the template genuinely reusable without modification.

---

### Exercise 2: Data Extraction Template

An unstructured text extraction template was created and validated across three different sentence structures.

**Template:** *"Extract the following fields from the text: Name, Age, Location, Occupation. Return the output in JSON format."*

All three inputs returned clean, consistent JSON:

```json
{
  "Name": "...",
  "Age": ...,
  "Location": "...",
  "Occupation": "..."
}
```

Test 3 deliberately used a different sentence order (*"Victoria Ifeoma works as a data scientist. She is 23..."*) to stress-test the template — the model still extracted all four fields correctly.

**Key Takeaway:** The template works regardless of how information is arranged in the source text. The JSON format makes outputs machine-readable and directly usable in databases or applications, showing how a well-structured extraction pattern adds both consistency and practical utility.

---

### Exercise 3: Prompt Transformation with Patterns

A vague prompt was transformed using two different pattern types and the improvement was documented.

**Vague prompt:** *"Write about climate change."*

| Pattern | Transformed Prompt | Output Style |
|---|---|---|
| **Instructional** | *"Explain climate change in 3 paragraphs for business professionals who need to understand corporate sustainability"* | Audience-specific, structured by business context → corporate response → strategic outlook |
| **Comparative** | *"Compare climate change impacts on developed vs developing nations in 5 bullet points"* | Side-by-side comparison across 5 dimensions: economic resilience, agriculture, health, displacement, historical responsibility |

**Key Takeaway:** The vague prompt gave no direction on audience, format, or angle. The instructional pattern locked in a specific audience and structure, producing a focused and actionable response. The comparative pattern forced a structured side-by-side analysis that would be impossible to achieve consistently with an open-ended request. Both transformations show that adding clear constraints — audience, format, scope — consistently elevates output quality.

---

## Resources

- [Learn Prompting – Prompt Patterns](https://learnprompting.org/docs/prompt_hacking/offensive_measures/prompt_injection)
- [Prompt Engineering Guide – Templates](https://www.promptingguide.ai/techniques/prompt_chaining)
- [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)

## Author

**jmomoh** — Learn2Earn Academy
