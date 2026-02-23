# AI Ethics

A deep, self-reflective exploration of responsible AI use, bias detection, ethical prompt design, and using AI as a learning amplifier rather than a shortcut.

## Overview

This quest goes beyond technical prompting to address the foundational question: *how* should you use AI as a developer? Topics covered include:

- Principles of responsible AI use: fairness, transparency, and accountability
- Identifying bias in datasets and model outputs
- Designing prompts that are safe, clear, and free from harmful assumptions
- Handling sensitive or incorrect model outputs responsibly
- The critical difference between using AI to learn vs. using AI to avoid learning

## Learning Objectives

By the end of this quest, you will be able to:

- Understand the basic principles of AI ethics and responsible use
- Identify common types of bias in datasets and model outputs
- Design prompts that are transparent, safe, and free from harmful assumptions
- Handle sensitive or incorrect model outputs responsibly
- Develop skills that make you irreplaceable as a coder

## Requirements

- Python 3.9+ (optional)
- Browser with access to an LLM interface (ChatGPT, Claude, etc.)
- No complex environment setup required

## Setup

1. **Clone the repository**
   ```bash
   git clone https://acad.learn2earn.ng/git/jmomoh/ai-ethics
   cd ai-ethics
   ```

2. **Verify Python version (optional)**
   ```bash
   python --version
   # Expected: Python 3.9+
   ```

## Project Files

```
ai-ethics/
├── README.md
├── .gitignore
├── ex00_ai_ethics_coder.md   ← Personal fairness contract + self-assessment
└── isPalindrome.py            ← Palindrome implementation from Exercise 00
```

---

## Exercises

### Exercise 00: Learning to Use AI Ethically as a Coder

A full self-assessment and practical challenge on the *right* way to use AI as a developer.

**Self-assessment findings:**
- Honest identification of current pattern: mostly Learner A (using AI as an answer generator when frustrated)
- Palindrome challenge completed independently first — pseudocode written, bugs debugged manually, then AI used only to explore complexity and edge cases

**Palindrome solution (built independently):**
```python
def isPalindrome(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")
```

**Extended version (handles punctuation + returns failure position):**
```python
def palindrome(text):
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    for i in range(len(cleaned_text) // 2):
        if cleaned_text[i] != cleaned_text[len(cleaned_text) - 1 - i]:
            return i  # position where palindrome breaks
    return True
```

**Personal Fairness Contract** (see `ex00_ai_ethics_coder.md`):

| I WILL use AI when | I will NOT use AI when |
|---|---|
| After attempting for at least 20 minutes | I haven't tried the problem myself |
| To understand why my solution works/doesn't | During assessments or tests |
| To explore alternatives after a working solution | Building core fundamentals |
| To debug after writing out my thought process | The struggle is teaching me something important |

*Signed: JEZREAL OSEIWE MOMOH — 13-02-2026*

**Key Takeaway:** Struggling through the palindrome first built genuine understanding. The difference between Learner A and Learner B is not whether you use AI — it's *when* and *why* you use it.

---

### Exercise 1: Understanding AI Bias

**Bias example identified independently:** Asking AI for "the greatest leaders of all time" returned predominantly male leaders — not because of intentional design, but because historical records and training data reflect centuries of gender exclusion from documented leadership roles.

**Root cause:** AI reflects and amplifies historical inequality in its training data, not just current bias.

**Mitigation proposed:** Reframe the prompt — *"Provide 5 male and 5 female influential leaders throughout history"* — to force balanced representation.

**AI deepened understanding by identifying:**
- Power structures and language dominance in historical records
- Feedback loops that reinforce bias even in recent data
- Real-world implications in healthcare (misdiagnosis), hiring (qualified candidates filtered out), and criminal justice (wrongful identification)

**Key Takeaway:** AI doesn't create bias from nothing — it learns from human history. Mitigation starts with the prompt, but understanding *why* the bias exists requires knowing the history behind the training data.

---

### Exercise 2: Designing Ethical Prompts

Three problematic prompts were identified, analysed, and rewritten independently before AI critique.

| Original Prompt | Core Problem | Improved Prompt |
|---|---|---|
| *"Describe a typical user of a tech app"* | Assumes a single "typical" user, erases diversity | *"Describe a diverse range of user profiles for a banking application, considering various demographics and needs"* |
| *"Why are men better at soccer than women"* | Assumes male superiority as fact, biological determinism | *"Compare the evolution and support systems of men's and women's soccer"* |
| *"How can I scam people like Nigerians do"* | Requests illegal activity + links nationality to crime | *"What are common types of online scams and how can people protect themselves"* |

All three improved prompts were tested and confirmed to produce safer, fairer, more useful outputs.

**Key Takeaway:** Ethical prompt design means removing hidden assumptions, reframing superiority claims as comparative questions, and redirecting harmful requests toward constructive ones. Writing poor prompts first and fixing them builds a much deeper understanding of *why* the improvements matter.

---

### Exercise 3: Detecting and Mitigating Harmful Outputs

The biased prompt *"Why are men better at soccer than women"* was used as a safety test case to identify all output risks.

**Issues identified:**
- Factual error: presents an unverified assumption as answerable fact
- Potential harm: reinforces gender stereotypes, devalues women athletes
- Missing context: no acknowledgement of historical investment gaps or structural inequality
- Overconfidence: implies a definitive answer exists where none does

**Revised prompt:** *"How have historical investment, training opportunities, and social support shaped the development of men's and women's soccer?"*

**Real-world harmful AI case referenced:**  
A Centre for Countering Digital Hate study found AI chatbots giving unsafe self-harm advice to teenagers.  
Source: [counterhate.com/research/fake-friend-chatgpt](https://counterhate.com/research/fake-friend-chatgpt)

**Key Takeaway:** Relying on AI to detect AI's own problems is fundamentally flawed — AI can replicate the same biases it's evaluating. Human critical thinking, ethical judgment, and fact-checking remain irreplaceable.

---

### Exercise 4: AI as Learning Amplifier

**Topic:** Wireless routing protocols applied to a real smart-city IoT network design.

**Smart-city network designed (1,000 IoT sensors, 50 traffic lights, 10 emergency vehicles):**

| Device / Layer | Protocol | Justification |
|---|---|---|
| IoT Sensors | LoRaWAN / Zigbee | Low power, long battery life, city-wide coverage |
| Traffic Lights | Wi-Fi 6 / LTE / 5G | Fast, reliable, real-time control |
| Emergency Vehicles | 5G / LTE with QoS priority | Mobile, low latency, priority preemption |
| Sensor → Gateway | MQTT | Lightweight publish/subscribe, scales to thousands of devices |
| Gateway → Cloud | HTTPS / MQTT over TCP | Secure, reliable, analytics-ready |

**Failure points identified:** Power outage, device malfunction, security breaches, network congestion.

**Reflection:**
- Human judgment vs. AI contribution: ~40% / 60%
- AI sharpened reasoning by questioning assumptions and highlighting trade-offs — it did not replace judgment
- Core protocol behaviours, design trade-offs, and IoT principles expected to be retained long-term

---

## Resources

- [OECD Principles on AI](https://oecd.ai/en/ai-principles)
- [UNESCO AI Ethics Recommendation](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics)
- [Microsoft Responsible AI Standard](https://www.microsoft.com/en-us/ai/responsible-ai)
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Hugging Face Ethics](https://huggingface.co/blog/ethics-soc-2)

## Author

**jmomoh** — Learn2Earn Academy
