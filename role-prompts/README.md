# Role Prompts

A practical exploration of role-based and tone-driven prompt engineering using Python and AI language models.

## Overview

This project dives into how defining roles and personas inside prompts can shape the style, tone, and reasoning of AI model responses. Topics covered include:

- Simulating personas: expert, assistant, critic, and more
- Injecting tone and perspective into model responses
- Comparing how role instructions shift output focus and language

## Learning Objectives

By the end of this quest, you will be able to:

- Write prompts that change tone (friendly vs professional)
- Create expert personas for tasks (e.g., lawyer, recruiter, tutor)
- Compare how role instructions influence outputs

## Requirements

- Python 3.9+
- `numpy`
- `pandas`
- `jupyter`
- OpenAI Playground or ChatGPT interface

## Setup

1. **Clone the repository**
   ```bash
   git clone https://acad.learn2earn.ng/git/jmomoh/role-prompts
   cd role-prompts
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

## Project Structure

```
role-prompts/
├── README.md
├── .gitignore
└── exercises/
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

### Exercise 1: Simulating Multiple Roles

The same question — *"What is climate change?"* — was sent to the model three times, each time with a different role assigned.

| Persona | Tone | Focus |
|---|---|---|
| **Scientist** | Objective, technical, data-driven | Radiative forcing, CO₂ ppm, feedback loops |
| **Journalist** | Accessible, narrative, public-facing | Real-world impacts, policy context, human stories |
| **Critic** | Skeptical, argumentative, questioning | Challenging assumptions, questioning consensus framing |

**Key Takeaway:** Role instructions don't just change tone — they change *which facts get highlighted* and *how reasoning is framed*. Each persona filters the same topic through a different lens.

---

### Exercise 2: Role-Based Mentoring and Feedback

A Python function with intentional bugs was submitted to the model with the prompt:
> *"Act as a mentor reviewing this code. Provide corrections and explain improvements."*

**Bugs found and corrected:**

1. **Wrong `.replace()` logic** — `"A < Z"` is not valid Python; replaced with a proper character filter using `c.isalnum()`.
2. **Assignment vs. comparison** — `=` changed to `==` inside the `if` statement.
3. **Inconsistent indentation** — standardized to 4 spaces throughout.

**Corrected function:**
```python
def palindrome(text):
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False

word = input("Enter your text: ")
print("Palindrome!" if palindrome(word) else "Not a palindrome!")
```

**Key Takeaway:** Assigning the mentor role caused the model to prioritize *teaching and encouragement* over simply fixing the code. The feedback was structured, step-by-step, and focused on building understanding — not just providing an answer.

---

### Exercise 3: Tone Variation with the Same Task

Task: *"Write an email inviting a candidate to an interview for a software developer position."*

| Prompt | Tone | Style |
|---|---|---|
| *"Write a friendly tone email..."* | Warm, casual, conversational | Shorter sentences, encouraging language, informal greeting |
| *"Write a professional tone email..."* | Formal, structured, precise | Business language, detailed expectations, formal sign-off |

Both emails communicated the same core information — the invitation, role title, interview details, and next steps — but the *emotional framing* was completely different.

**Key Takeaway:** Tone instructions change how a message *feels* without changing its *purpose*. The friendly version builds approachability; the professional version signals formality and clear expectations.

---

## Resources

- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Prompt Engineering Guide – Personas](https://www.promptingguide.ai/techniques/personas)
- [Anthropic Prompt Library](https://docs.anthropic.com/en/prompt-library/library)

## Author

**jmomoh** — Learn2Earn Academy
