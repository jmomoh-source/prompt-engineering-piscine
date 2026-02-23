# Debug Control

A practical exploration of techniques for detecting, preventing, and correcting misleading or inaccurate AI outputs.

## Overview

This project focuses on how prompt design choices can either invite or prevent AI hallucinations and fabricated information. Topics covered include:

- How to detect and fix misleading or inaccurate outputs
- Anchoring responses to data, constraints, or reference material
- Using delimiters and formatting to keep responses on topic

## Learning Objectives

By the end of this quest, you will be able to:

- Spot vague or fabricated information in outputs
- Rewrite prompts to add clear constraints
- Use delimiters and formatting to keep responses on topic

## Requirements

- Python 3.9+
- `numpy`
- `pandas`
- `jupyter`
- OpenAI Playground or ChatGPT interface

## Setup

1. **Clone the repository**
   ```bash
   git clone https://acad.learn2earn.ng/git/jmomoh/debug-control
   cd debug-control
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

### Exercise 1: Reducing False or Invented Facts

A problematic prompt was rewritten to ground the question in a real, verifiable subject.

| Prompt | Subject | Output Quality |
|---|---|---|
| *"Who is the president of Zootopia?"* | Fictional place | Model correctly flagged it as fictional — but risky, as it could have hallucinated |
| *"Who is the president of Kuwait?"* | Real country | Factual response, correctly clarified Kuwait has an Emir not a president |

**Key Takeaway:** Asking about fictional or ambiguous subjects opens the door to hallucination. Grounding prompts in real, verifiable subjects forces the model to produce factual, checkable responses and reduces the risk of invented information.

---

### Exercise 2: Adding Source or Data Constraints

Three versions of the same question were tested against a provided passage about Jollof rice, with increasing levels of constraint.

| Prompt Version | Constraint | Result |
|---|---|---|
| No constraint | None | Added external information not in the passage (social media, #JollofWars hashtag) |
| *"Use only the text provided below"* | Source-bounded | Stayed strictly within the passage, no external additions |
| *"Cite specific details from the source"* | Source-cited | Used direct quotations and explicitly attributed each claim to the source |

**Key Takeaway:** Without constraints, the model freely added external knowledge that may be accurate but is unverifiable from the given text. Adding *"use only the text provided"* eliminated outside additions entirely. Adding a citation instruction further improved accountability by making it clear exactly which information came from the source — essential for academic or formal contexts.

---

### Exercise 3: Using Delimiters to Define Context

The same passage was provided with and without `###` delimiters to test how boundaries affect output scope.

| Prompt | Format | Output |
|---|---|---|
| Without delimiters | Plain context block | Listed 5 ingredients from the text, then added 10+ modern ingredients not in the passage |
| With `###` delimiters + *"Answer using ONLY the text inside the delimiters"* | Delimited block | Listed only the 5 ingredients explicitly stated in the passage |

**Key Takeaway:** Without delimiters, the model treated the context as a starting point and supplemented it with outside knowledge. Adding `###` delimiters combined with a clear boundary instruction created a strict scope that prevented the model from going beyond what was explicitly written — making outputs precise and fully verifiable.

---

## Resources

- [Learn Prompting – Avoiding Hallucinations](https://learnprompting.org/docs/reliability/hallucinations)
- [Prompt Engineering Guide – Robustness](https://www.promptingguide.ai/techniques/consistency)
- [Preventing LLM Hallucination](https://www.ibm.com/topics/ai-hallucinations)

## Author

**jmomoh** — Learn2Earn Academy
