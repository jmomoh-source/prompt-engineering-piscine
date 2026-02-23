# Creative AI

A hands-on exploration of generative prompting for creative text, professional content, and image generation.

## Overview

This project applies prompt engineering to real-world creative use cases, from storytelling and resume writing to designing descriptive prompts for image generation models. Topics covered include:

- Generative prompts for text and creative outputs (stories, visuals, marketing)
- Applied prompting for real-world use cases such as UX, resumes, ideation, and design

## Learning Objectives

By the end of this quest, you will be able to:

- Write prompts for creative generation tasks
- Personalize prompts for industry-specific applications
- Explore prompts for both text-based and image-based models

## Requirements

- Python 3.9+
- `numpy`
- `pandas`
- `jupyter`
- OpenAI Playground or ChatGPT interface
- Image model interface (e.g., DALL·E, Stable Diffusion)

## Setup

1. **Clone the repository**
   ```bash
   git clone https://acad.learn2earn.ng/git/jmomoh/creative-ai
   cd creative-ai
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

### Exercise 1: Generating a Short Story from a Theme

Three different themes were tested using the same base prompt structure to compare how theme drives tone and genre.

**Base prompt:** *"Write a short story about [theme] in under 300 words."*

| Theme | Genre/Tone | Setting | Word Count |
|---|---|---|---|
| Interstellar | Epic sci-fi, emotional sacrifice narrative | Space / Lagos | 248 |
| Psychosis | Dark psychological horror | Lagos flat & market | 238 |
| Déjà Vu | Mysterious, philosophical loop tale | Lagos streets & market | 246 |

All three stories naturally incorporated Lagos-based settings, showing the AI maintained consistent contextual patterns while adapting genre and emotional tone entirely to the theme.

**Key Takeaway:** A single clear theme word is enough to shift the entire tone, vocabulary, and narrative structure of the output. Sci-fi themes produced technical, cosmic language; psychological themes produced tense, sensory writing; mystery themes produced philosophical, introspective prose. Theme is one of the most powerful creative controls available in a prompt.

---

### Exercise 2: Personalized Resume Summary

The same resume summary prompt was adapted for two different professional roles to observe how the AI adjusts language and emphasis.

| Role | Prompt Focus | Output Style |
|---|---|---|
| DevOps Engineer | Python, cloud systems, CI/CD | Technical jargon, quantified metrics (60% faster deployments, 99.9% uptime) |
| Teacher | Physics, Chemistry, conversational skills | Soft skills focus, emotional impact language ("passionate", "ignite curiosity") |

**Key Takeaway:** The AI automatically calibrates vocabulary, tone, and evidence type to the role — technical roles get tools, frameworks, and numbers; education roles get human-centred, impact-driven language. Simply specifying the role and relevant skills is enough to unlock a professionally appropriate, field-specific summary.

---

### Exercise 3: Image Generation Prompt Design

A vague image prompt was refined with specific constraints to demonstrate how descriptive detail directly controls creative output.

| Prompt Type | Prompt | Result |
|---|---|---|
| **Vague** | *"Generate a futuristic city at sunset image"* | Clean aerial view, utopian skyline, sleek glass towers, generic sci-fi feel |
| **Refined** | *"Futuristic city skyline at sunset in vibrant graffiti art style, viewed from street level. Towering skyscrapers covered in neon tags and murals, flying cars leaving light trails, holographic billboards flickering. Bold spray-paint textures with electric blues, hot pinks, and gold accents."* | Gritty cyberpunk streetscape, graffiti-covered buildings, chaotic neon energy, strong urban rebellion atmosphere |

**Key Takeaway:** The vague prompt defaulted to a generic, clean sci-fi interpretation. The refined prompt's explicit constraints — art style (graffiti), viewpoint (street level), mood (rebellion), and colour palette — each translated directly into visible elements in the final image. Descriptive prompts give precise creative control; vague prompts hand that control entirely to the model.

---

## Resources

- [106 Prompts for Creativity](https://www.creativebloq.com/features/chatgpt-prompts-for-creatives)
- [Awesome ChatGPT Prompts – Creative Uses](https://github.com/f/awesome-chatgpt-prompts)
- [DALL·E Prompt Book](https://dallery.gallery/the-dalle-2-prompt-book/)

## Author

**jmomoh** — Learn2Earn Academy
