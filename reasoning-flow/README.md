# Reasoning Flow

A hands-on exploration of chain-of-thought prompting techniques using Python and AI language models.

## Overview

This project focuses on how structured prompts can guide AI models to "think out loud" and show their reasoning process step by step. Topics covered include:

- Boosting reasoning with step-by-step logic
- Letting the model expose intermediate reasoning before final answers
- Breaking complex multi-step problems into smaller, verifiable parts

## Learning Objectives

By the end of this quest, you will be able to:

- Apply chain-of-thought prompting to math, logic, and coding problems
- Encourage reasoning before final answers with structured prompts
- Create multi-step prompts for solving complex questions

## Requirements

- Python 3.9+
- `numpy`
- `pandas`
- `jupyter`
- OpenAI Playground or ChatGPT interface

## Setup

1. **Clone the repository**
   ```bash
   git clone https://acad.learn2earn.ng/git/jmomoh/reasoning-flow
   cd reasoning-flow
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

### Exercise 1: Logic Puzzle with Explanation

A custom logic puzzle was used to compare outputs with and without reasoning instructions.

**Puzzle:** *"Jonathan scored higher than Tiwa. Ibrahim scored lower than Tiwa but higher than John. Who scored the lowest?"*

| Prompt | Output |
|---|---|
| Without reasoning | *"John scored the lowest."* — answer only, no explanation |
| With *"Explain your reasoning before giving the final answer"* | Full step-by-step ranking: Jonathan → Tiwa → Ibrahim → John |

**Key Takeaway:** Without reasoning instructions, the model skips straight to the answer. Adding "explain your reasoning" forced the model to surface each logical relationship, making the conclusion easy to verify and understand.

---

### Exercise 2: Step-by-Step Reasoning Prompt

The same math problem was submitted with and without the chain-of-thought trigger phrase.

**Problem:** *"Calculate the factorial of 10"*

| Prompt | Output |
|---|---|
| Without reasoning | `10! = 3,628,800` — final answer only |
| With *"Let's think step by step"* | Definition of factorial → each multiplication step from 10×9 down to ×1 → final answer |

**Key Takeaway:** The phrase *"Let's think step by step"* is a simple but powerful trigger. It shifted the model from answer-delivery mode into a teaching mode where each intermediate calculation was shown and could be verified independently.

---

### Exercise 3: Multi-Step Question Answering

A structured prompt with explicit instructions was used to break a calculation into stages.

**Problem:** *"What is 25% of the sum of 30 and 70?"*

**Structured prompt instructions given:**
1. Restate the problem in your own words
2. Break it into smaller steps
3. Solve each step before moving to the next
4. Provide the final answer

**Model output followed all four instructions:**
- Restatement → find 25% of the total of 30 and 70
- Step A → 30 + 70 = 100
- Step B → 25% of 100 = 0.25 × 100 = **25**

**Key Takeaway:** Providing an explicit structure inside the prompt — restate, break down, solve, answer — produced a fully transparent solution. Each intermediate result could be checked, making it far easier to catch errors in more complex problems than a direct single-step answer would allow.

---

## Resources

- [Learn Prompting – Chain of Thought](https://learnprompting.org/docs/intermediate/chain_of_thought)
- [Prompt Engineering Guide – Reasoning Prompts](https://www.promptingguide.ai/techniques/cot)
- [Anthropic Prompt Library – Reasoning Examples](https://docs.anthropic.com/en/prompt-library/library)

## Author

**jmomoh** — Learn2Earn Academy
