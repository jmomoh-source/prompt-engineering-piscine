# Ethical AI

A foundational quest on building the right habits for lifelong learning — using AI as a learning amplifier, not a shortcut.

## Overview

Before diving into technical AI topics, this quest addresses something more fundamental: *how* to use AI without becoming dependent on it. The core challenge is developing judgment, systems thinking, and deep understanding — the skills that make a coder irreplaceable.

## Learning Objectives

By the end of this quest, you will be able to:

- Understand the difference between using AI to get answers and using AI to learn
- Practice the right workflow: attempt → verify → reflect
- Build a personal code of ethics for AI use in learning
- Recognize the professional risks of over-reliance on AI
- Identify the human skills that make coders irreplaceable

## Requirements

- Python 3.9+
- Access to a language model (ChatGPT, Claude, etc.) — but only *after* your first attempt at each exercise

## Setup

1. **Clone the repository**
   ```bash
   git clone https://acad.learn2earn.ng/git/jmomoh/ethical-ai
   cd ethical-ai
   ```

2. **Verify Python version**
   ```bash
   python --version
   # Expected: Python 3.9+
   ```

## Repository Structure

```
ethical-ai/
├── README.md
├── quest00/
│   ├── ex00_reflection.md
│   ├── ex01_palindrome.md
│   ├── ex02_variations.md
│   ├── ex03_fairness_contract.md
│   ├── ex04_scenarios.md
│   └── ex05_irreplaceable_skills.md
```

---

## What I Learned About AI and Self-Reliance

The most important lesson from this quest is that the *order* of how you use AI matters as much as whether you use it. Attempting problems first — even imperfectly — builds a mental model that makes AI feedback genuinely useful. Without that foundation, AI responses are just code to copy without context. With it, AI becomes a mirror that reflects gaps in your own thinking, suggests edge cases you missed, and opens up approaches you wouldn't have found alone.

The palindrome challenge made this concrete. Writing pseudocode first, struggling through bugs, and testing manually built an understanding of string comparison and indexing that no amount of copy-pasting could have given. When AI then pointed out the print statement issue and the `0`/`False` boolean trap, it landed — because there was already something to attach it to.

---

## Exercises

### Exercise 0: Honest Reflection
Identified current pattern as primarily **Learner B** — attempting problems first, using AI to deepen understanding rather than replace effort. Honest acknowledgement that frustration sometimes pulls toward shortcuts, and the goal is to close that gap consistently.

### Exercise 1: The Palindrome Challenge

**Solution built independently:**
```python
def palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False

word = input("enter your text: ")
print("palindrome" if palindrome(word) else "it is not palindrome")
```

**After strategic AI use — learned:**
- Time complexity: O(n) — each operation (replace, lower, reverse, compare) scans the string once
- Edge cases missed: punctuation, special characters, empty strings, strings of only spaces
- Better approach introduced: two-pointer method (avoids creating a reversed copy)

### Exercise 2: Strengthening Through Variations

Extended the palindrome function to handle punctuation, case sensitivity, and return the *position* where the string stops being a palindrome:

```python
def palindrome(text):
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    for i in range(len(cleaned_text) // 2):
        if cleaned_text[i] != cleaned_text[len(cleaned_text) - 1 - i]:
            return i
    return True
```

**AI identified:** the print statement wasn't using the position return value, and mixing `int` and `bool` returns (`0` evaluates as `False` in Python) — a subtle but important bug that independent testing hadn't caught.

### Exercise 3: The Fairness Contract

Personal rules for ethical AI use (full contract in `ex03_fairness_contract.md`):

| I WILL use AI when | I will NOT use AI when |
|---|---|
| I've tried the problem myself first | I haven't attempted it on my own |
| I need to understand *why* something works | Taking an exam or assessment |
| Exploring alternative approaches | Still building fundamental concepts |

*Signed: Jezreal Oseiwe Momoh — 11-02-2026*

### Exercise 4: Real-World Scenarios

Three scenarios were analysed to understand the real cost of over-reliance:

- **Interview (caching system design):** Without genuine understanding, you can name a concept but not explain it — and interviewers can tell the difference immediately.
- **Production bug at 2 AM, AI offline:** If you never understood the code, you can't debug it. If you used AI to *learn* the code, you can trace through the logic and fix it.
- **New library with no AI training data:** Reading official documentation, experimenting, and connecting to related knowledge — skills only built by learning independently first.

### Exercise 5: Building Irreplaceable Skills

| Skill | Rating |
|---|---|
| Problem Decomposition | 4/5 |
| Systems Thinking | 4/5 |
| Critical Evaluation | 3/5 |
| Debugging Mindset | 3/5 |
| Conceptual Understanding | 4/5 |

**Improvement plan for lowest-rated skills (Critical Evaluation & Debugging Mindset):**
1. Read and understand error messages fully before seeking any help — write out the failing line and the suspected reason
2. Rewrite code twice a week and use print statements to trace variable values step by step
3. Spend a minimum of 20 minutes testing code with different inputs before moving on, noting patterns and unexpected behaviour

---

## Main Insight

The question is never *whether* to use AI — it's *when*. Used after genuine effort, AI accelerates and deepens learning. Used instead of effort, it produces code you cannot defend, debug, or build on. The difference compounds over time: one path builds irreplaceable judgment, the other builds dependency.

## Applying These Principles in Future Quests

Going forward, every exercise will follow the same sequence: write pseudocode or an outline first, attempt an implementation, test it manually, document what's confusing — and *then* bring AI in to check assumptions, suggest edge cases, and explore alternatives. AI feedback only sticks when there's already something to attach it to. This quest established that habit, and the goal is to make it automatic across every technical challenge ahead.

---

## Resources

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [HackerRank](https://www.hackerrank.com) — practice problems for building fundamentals
- [Codewars](https://www.codewars.com) — kata-based coding challenges
- [Python Official Documentation](https://docs.python.org/3/)

## Author

**jmomoh** — Learn2Earn Academy
