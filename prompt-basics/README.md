# Prompt Basics

A hands-on introduction to prompt engineering using Python and AI language models.

## Overview

This project explores the fundamentals of prompting large language models (LLMs). Topics covered include:

- What a prompt is and how it works
- Anatomy of a prompt (system, user, and assistant messages)
- Zero-shot vs few-shot prompting
- Introduction to completions in ChatGPT / Playground

## Learning Objectives

By the end of this quest, you will be able to:

- Understand the structure and components of a prompt
- Distinguish between zero-shot and few-shot prompting
- Practice generating consistent outputs with simple prompts
- Explore how parameters like `temperature` and `top-p` affect model behavior

## Requirements

- Python 3.9+
- `numpy`
- `pandas`
- `jupyter`
- OpenAI Playground or ChatGPT interface

## Setup

1. **Clone the repository**
   ```bash
   git clone https://acad.learn2earn.ng/git/jmomoh/prompt-basics
   cd prompt-basics
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

### Exercise 1: Simple Prompt Writing
Wrote and compared two prompt styles:

- **Direct Instruction** — *"List 5 engineering tools"*  
  Produced a concise, focused response with minimal explanation.

- **Question Style** — *"What are the benefits of a healthy diet?"*  
  Produced a detailed, exploratory response with categories and context.

**Key Takeaway:** Direct instructions yield precise outputs; question-style prompts yield broader, more explanatory responses.

---

### Exercise 2: Instruction Refinement
Refined a vague prompt step by step to observe how specificity improves output quality.

| Prompt | Output Style |
|---|---|
| *"Tell me about AI."* | Broad overview with key areas and applications |
| *"Explain AI in simple terms for beginners."* | Beginner-friendly, uses analogies, avoids jargon |
| *"Summarize the main AI techniques in 5 bullet points."* | Structured, concise, technically focused |

**Key Takeaway:** Adding constraints like audience level or output format makes responses more targeted and useful.

---

### Exercise 3: Parameter Experimentation
Tested how `temperature` and `top-p` affect model output using the same prompt.

| Parameter | Value | Output Style |
|---|---|---|
| Temperature | 0.2 | Precise, consistent, technical |
| Temperature | 0.9 | Creative, expressive, metaphorical |
| Top-p | 0.5 | Safe, predictable word choices |
| Top-p | 1.0 | Diverse vocabulary, philosophical tone |

**Key Takeaway:** `temperature` controls creativity/randomness; `top-p` controls the breadth of word selection. Lower values = precision; higher values = expressiveness.

---

## Resources

- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Anthropic – How to write prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Prompting Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)

## Author

**jmomoh** — Learn2Earn Academy
