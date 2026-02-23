# Ask the model to act as a coding mentor.
Prompt- "Act as a coding mentor"


# Python function with a bug.

def palindrome(text):
 # Remove spaces and convert to lowercase
    cleaned_text = text.replace("A < Z", "a < z").lower()
    
# Compare cleaned string forwards and backwards
    if cleaned_text = cleaned_text[::-1]:
        return True
    else: 
        return False

# input character to check or compare
word = input ("enter your text: ")


# MENTOR PROMPT: 

- "Act as a mentor reviewing this code. Provide corrections and explain improvements."

### Mentor Review/RESPONSE: Palindrome Function
Great effort Your logic is on the right track, but there are 3 bugs to fix. Let's work through them together:

***Bug 1:*** Wrong .replace() logic
# Your code:
cleaned_text = text.replace("A < Z", "a < z").lower()

# Should be:
cleaned_text = ''.join(c.lower() for c in text if c.isalnum())

Why: "A < Z" is not valid Python - it's trying to replace a literal string "A < Z" with "a < z", which doesn't exist in your input. You want to remove ALL non-alphanumeric characters and convert to lowercase.


***Bug 2:*** Assignment instead of comparison
python
# Your code:
if cleaned_text = cleaned_text[::-1]:

# Should be:
if cleaned_text == cleaned_text[::-1]:

***Why:*** Single = is assignment (storing a value). Double == is comparison (checking if equal). This is one of the most common Python mistakes!


***Bug 3:*** Indentation Issues
python
# Your code:
def palindrome(text):
 # Remove spaces and convert to lowercase  ← 1 space indent
    cleaned_text = ...  ← 4 space indent (inconsistent!)

***Why:*** Python requires consistent indentation. Use 4 spaces throughout your function.

# CORRECTED VERSION:

def palindrome(text):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    
    # Compare cleaned string forwards and backwards
    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False

# Input character to check or compare
word = input("enter your text: ")
print("Palindrome!" if palindrome(word) else "Not a palindrome!")



# Review the response and check if the role influences feedback style.

The response was absolutely supportive, encouraging, and educational rather than simply corrective. It praised my effort first and guided me through mistakes step by step. Instead of only giving me the fixed code, it explained why each issue occurred and the explanation focused on learning outcomes, not just fixing the bug.

### The Structure:
The feedback was organized into clear sections (Bug 1, Bug 2, Bug 3), making it easier to follow and learn from. Followed by the corrected version and explanations of my mistakes.

### Key Influence of the Role:
Acting as a mentor caused the AI to prioritize teaching, encouraging, and reasoning over speed, the response is aimed at building my understanding and confidence rather than just providing the answer.



