# Tool Prompts

A hands-on introduction to using language models with external tools, structured outputs, and chained prompt workflows.

## Overview

This project explores how prompts can be designed to produce machine-readable outputs and simulate tool-using agent flows. Topics covered include:

- Using language models with external tools (calculator, search, API)
- Basics of function calling for structured responses
- Chaining multiple prompts to mimic simple agent workflows

## Learning Objectives

By the end of this quest, you will be able to:

- Understand prompt chaining and tool use
- Design prompts that request structured JSON output
- Simulate API calls with controlled prompts
- Combine multiple prompts to mimic simple agent flows

## Requirements

- Python 3.9+
- `numpy`
- `pandas`
- `jupyter`
- OpenAI Playground or ChatGPT interface

## Setup

1. **Clone the repository**
   ```bash
   git clone https://acad.learn2earn.ng/git/jmomoh/tool-prompts
   cd tool-prompts
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

### Exercise 1: Structured JSON Output

An unstructured prompt was rewritten to enforce a specific JSON schema, then tested across three different domains.

**Unstructured prompt:** *"List 3 southern Nigeria states and their populations"*
→ Output: narrative text with approximate ranges, hard to parse programmatically

**Structured prompt:** *"List 3 southern Nigeria states and their populations. Return the data in JSON format with this structure: [{"state": "string", "population": number}]"*
→ Output: clean, valid JSON with consistent field types

**Tests across domains:**

| Test | Topic | Schema Used |
|---|---|---|
| Test 1 | Nigerian states & populations | `state`, `population` |
| Test 2 | Programming languages & release years | `Programming Language`, `Release year` |
| Test 3 | Cybersecurity tools & features | `Tools`, `Features` |

All three tests returned valid, consistently structured JSON.

**Key Takeaway:** Specifying the exact JSON schema inside the prompt guarantees machine-readable output with predictable field names and data types — critical for any workflow that needs to pass data between systems or parse responses programmatically.

---

### Exercise 2: Simulated API Call (Weather Example)

A reusable prompt template was created to simulate weather API responses and tested across four cities.

**Reusable template:**
```
Simulate a weather API response for [CITY] today in JSON format with this structure:
{"location": <string>, "temperature_celsius": <number>, "condition": <string>}
```

**Test results:**

| City | temperature_celsius | condition |
|---|---|---|
| Paris | 8.5 | partly cloudy |
| Ontario | -3.2 | snow showers |
| Lagos | 29.8 | scattered thunderstorms |
| London | 7.2 | light rain |

All four outputs matched the defined schema exactly — same field names, same data types, consistent structure.

**Key Takeaway:** The weak prompt produced unstructured, unpredictable text. Defining the expected schema explicitly in the prompt ensured every city returned the same three fields in the same format, making the output reliably parseable and suitable for simulating real API integrations.

---

### Exercise 3: Chaining Prompts for Agent Flow

Three prompts were chained together to simulate how a real AI agent processes a user's natural language request end to end.

**Complete chain:**

```
User Query → [Step 1: Parse Intent] → [Step 2: Fetch Data] → [Step 3: Format Response] → Final Answer
```

| Step | Prompt Goal | Output |
|---|---|---|
| Step 1 | Extract city and intent from the user query | `{"city": "Paris", "intent": "current temperature"}` |
| Step 2 | Simulate weather API call using extracted city | `{"location": "Paris", "temperature_celsius": 8.5, "condition": "partly cloudy"}` |
| Step 3 | Convert structured data into a natural language reply | *"The temperature in Paris is currently 8.5°C with partly cloudy conditions."* |

**Key Takeaway:** Each step in the chain depends on the structured output of the previous one — if any step produces malformed JSON, the entire flow breaks. This exercise demonstrated why precise output formatting at every stage matters, and how breaking a complex task into smaller focused steps makes the workflow easier to build, test, and debug — the same principle behind real-world AI agent design.

---

## Resources

- [Prompt Engineering Guide – Function Calling](https://www.promptingguide.ai/applications/function_calling)
- [OpenAI Cookbook – Function Calling Basics](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models)
- [Awesome ChatGPT Prompts – Structured Output](https://github.com/f/awesome-chatgpt-prompts)

## Author

**jmomoh** — Learn2Earn Academy
