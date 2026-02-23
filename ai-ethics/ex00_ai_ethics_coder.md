# Part A: The Critical Distinction

## Write down your honest answers:

- How have you used AI for coding so far?

I try to attempt problems first, but honestly, about 80% of the time i get frustrated and just ask AI for the complete solution.


- Do you ask AI for solutions before trying yourself?

Sometimes Yes, and sometimes No, It depends on the task or problem. For example if it is something related to what i have done before i try at first. if it looks new and complex i just skip to shortcuts.


- Can you explain code you've submitted without AI's help?

For some codes Yes, Like my Go code because i had to studied it with my peers to learn the code. but for the codes i copied and pasted from AI i probably can't explian every detail without asking AI for help.


- What would happen if AI was suddenly unavailable during an exam or interview?

That would depend on the questions being asked if i have prior knowledge i would be able to explain but without Ai i wouldnt be able to explain some concepts, write syntax or codes from memory, it would take more time to debug some codes, and my problem solving approach might be longer and not efficient


## Identify your current pattern: Which learner are you now?

I would say learner A, basically because i am a learner and i often do ask AI fo the answers when i get fraustrated and submit those codes without fully understanding the code. Somehow i believe i am inbetween because of the palindrome challenge this time i can actually explain eachline of the code because i struggled through it.


- Write a brief paragraph: Where are you now, and where do you want to be?
Right now i often get frustrated and ask AI for complete solution, which leaves me at a disadvantage because i can't explain my code. But through the palindrome challenge struggling through problems built real understanding and genuine interest in knowing more. I want to become more independent and reliant on my self first before seeking AI as my learning tool and not a solution to my problem.


# Part B: The Wrong Way vs. The Right Way

Challenge: Implement a simple function to check if a string is a palindrome.

### Track A — The Wrong Way (observe but DO NOT do this):
- Noted

### Track B — The Right Way (DO THIS): 

## Step 1: My solution

### PSEUDOCODE:
- step 1:  Define the function "def isPalindrome". 
- step 2: Modify the Variable "s" by ignoring spaces and change characters fom uppercase to lowercase characters.
- step 3: compare strings to the reverse if they match 
- step 4: if it is a palindrome print Yes, if not print No
- step 4: user input.

### PYTHON IMPLEMENTATION:
def isPalindrome(s):

//Modify the Variable "s" by ignoring spaces and change characters fom uppercase to lower case.
    s = s.replace(" ","").lower()

//compare strings to the reverse if they match 
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")

word = input ("enter your string: ")
isPalindrome(word)

### TESTING RESULT
- "racecar" Yes
- "hello" No
- "A man a plan a canal Panama" Yes

### BUGS I ENCOUNTERED AND FIXED
I encountered nameErrors, 
indentation issues, 
reverse variable problem.


## Step 2: Strategic AI use After you have a working solution, ask AI:

### What's the time complexity?
O(n) where n is the length of the string.
this simply means if the string is twice as long , the function would take twice as long to run, which is good performance. 

### What edge cases am I missing?
My test result afer inputing an empty string is Yes.
I added punctuations and it returned "No" and should have been "Yes" because my ode only removes paces not punctuations.
I tested numbers "12321" and it returned "Yes"
To fix the punctuation mark i would need to import and apply a functuntion to i dentify punctuation haracters as well. 


### Alternatives and trade-offs?

- Alternative 1: Two-pointer approach

def isPalindrome(s):
    s = s.replace(" ", "").lower()
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

- Alternate 2: Using built-in reversed:

def isPalindrome(s):
    s = s.replace(" ", "").lower()
    return s == ''.join(reversed(s))

### How does it perform on very long strings?"
For a 1 million character string it still runs fast but it creates a full reversed copy, so uses 2X the memory


## Step 3: Reflection

- What did you learn by struggling first?
I learnt what palindome is all about, what makes it a palindrome and what doesn't, learnt how to structure my code using pseudocode, fom then i could easily tell which line of my code needed debugging.


- How is your understanding different than if you'd just asked for the solution?
Well if i had just copied and pasted i would only remember the name of the code, but strugglingling through it i can explain the ode and tell whih part of my code has errors that might need debugging.


- Can you now implement similar functions (reverse a string, find duplicates) without AI?
yes i can using python


- What mental model did you build?
Well i built a mental model of breaking down the problems into steps by writing the Pseudocode, Then understandingthe logic for which the code should run. Then testing the code running through series of problems to check if there are any more lines in my code i should modify and also when bugs appear i can trace through my code step by step because from my approach i understand what each line does.



# Part C: Testing Your Understanding

## MY MODIFIED PALINDROME FUNCTION

I completed all three variation without using AI first-- 

def palindrome(text):

    // Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    
    // Check if the cleaned text is a palindrome

    for i in range(len(cleaned_text) // 2):
        
        // Compare characters from the start and end
        if cleaned_text[i] != cleaned_text[len(cleaned_text) - 1 - i]:
            return i
    
    // If we reach here, it's a palindrome
    return True

### What my modifications do
- Ignores spaces and punctuation - uses `.isalnum()` to keep only letters and numbers
- Case-insensitive - uses `.lower()` to convert everything to lowercase
- Returns position where palindrome breaks - returns the index `i` where mismatch occurs

### Testing
- `"A man, a plan, a canal: Panama!"` → Returns `True` 
- `"hello!"` → Returns `0`
- `"race car"` → Returns `True`


## Strategic AI Question

- Did I miss any edge cases?
**Edge cases I might have missed:**
- Empty strings return `True` - which is acceptable
- All punctuation strings (like "!!!") become empty and return `True`
- Unicode characters are handled by `.isalnum()`

- How could I make this more efficient?
**Efficiency analysis:**
- My code is already O(n) time complexity, which is optimal
- Uses O(n) space for the cleaned string.
- The trade-off between memory and readability is good making it more memory efficient would make the code harder to understand.
- For most real-world use cases, my approach is the right balance.

My solution was already efficient and handled the requirements well enough. The main insight is that sometimes a more efficient code sacrifices readability for minimal performance gain, which is not always worth it.



# Part D: The Fairness Contract

### I will use AI when:

- After I've attempted a problem for at least 20 minutes
- To understand why my solution works/doesn't
- To explore alternatives after I have a working solution
- I require help debugging and understanding concepts of the problem
- i have writen out my thught process first and i can show that i have tried. 
- i have a working code and want to learn better approaches

### I will NOT use AI when:

- I haven't tried the problem myself
- I'm taking an assessment or test
- I need to build fundamentals
- when the struggle is teaching me something important even if it's frustrating.

### I know I'm using AI fairly when:

- I can explain my code without looking at AI's response
- I could solve similar problems without AI
- I feel more confident in my abilities
- i can explain or walk someone else through my code without notes.
- Debug my code without seeking assistance


Sign: JEZREAL OSEIWE MOMOH
Date: 13-02-2026


# Part E: Real-World Scenario Analysis

### Interview: "Explain how you'd implement a caching system." If you always relied on AI, can you answer?
If I've always relied on AI to design systems, I wouldn't be able to explain a caching system in an interview because i wouldn't know how to wite the code or how to debugg if an error pops up. I might know that caching exists, but wouldn't understand the syntax of the code. Using AI as a learning tool instead means i get to wite study practice debugg and run my code personally and that would instill the problem solving mentality we all aim for.

### Production bug at 2 AM: AI is unavailable. Can you debug code you don't fully understand?
If I relied on AI as a shortcut and just copied code without understanding it, I would NOT be able to debug it at 2 AM when AI is offline. I'd be stuck looking at code I don't understand. However, if I used AI as a learning tool and made sure I understood how the code works, then YES I could debug it because I understand the logic and can trace through it. My documentation would help remind me of the reasoning behind the code.


### New tech with little documentation: If you never learned to read docs and experiment, what happens?
I would read the documentation and do deep research on related libraries to understand it. Using AI as a learning tool taught me how to learn independently, break down problems and debug on my own, the skills i need when AI can't help.


### Write a paragraph: How does using AI fairly now prepare you for these scenarios?
Right now i often get frustrated and ask AI for complete solutions which leaves me at a disadvantage because i can't explain my code. But through the Palindrome challenge struggling thouh problems built my understanding and genuine interest in knowing more. I want to become more independent and reliant myself firt before seeking the help of AI as my learning tool and not a solution to my problems.



# Part F: Building Irreplaceable Skills

Rate yourself 1–5 and write an improvement plan for your lowest area:

- Problem decomposition 4/5

- Systems thinking 4/5

- Critical evaluation 3/5

- Debugging mindset 3/5

- Conceptual understanding (the "why") 4/5


### Action plan: 3 specific actions this week to improve it without outsourcing thinking to AI.

- i would read and understand error messages before seeking for help, i will write out the line that has the error and why i think my code failed.
- i will try rewriting at least one of my code twice a week and use print statements to trace each variable data or value.
- i would spend minimum of 20 minutes on my codes  and test it using different inputs to notices the patterns and where modification are needed.