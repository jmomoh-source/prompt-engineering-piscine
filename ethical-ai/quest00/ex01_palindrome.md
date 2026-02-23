### Step 1 - Pseudocode 
program
Function isPalindrome
Compare string with reversed string
if they match, return true
if they don't match return false


- Implement your solution in Python.

def palindrome(text):
 # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    
# Compare cleaned string forwards and backwards
    if cleaned_text == cleaned_text[::-1]:
        return True
    else: 
        return False

# input character to check or compare
word = input ("enter your text: ")


# checks if th sting is true or false and gives the result
print("palindrome" if palindrome(word) else "it is not palindrome")



### Step 2 - Use AI to learn

def palindrome(text):
    cleaned = text.replace(" ", "").lower()
    left = 0
    right = len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

# What's the time complexity?
linear time where n is string length. You scan the string multiple times (replace, lower, reverse, compare) but each is O(n), so overall O(n).

# What edge cases might I miss?
Punctuation: "A man, a plan, a canal: Panama" fails
Special characters: "race!car" fails
Empty string "" returns True
Only spaces "   " returns True

# Are there better approaches?"
YES


### Step 3 - Reflection

- What did you learn from solving it before asking AI?

i learnt what Palindrome is about, i wote my first pseudocode and used comment to express how the code function to even a non-programmer.

so the program checks through the string variable and compares if it matches from left to right, and prints a result as true if it is a palindrome or false if it is not


- How is your understanding different now?

My understaning is very broad now i have learnt how to check numbers or string characters in reverse and match them to be palindrome. also learnt something new in python  

- Could you now write similar functions (e.g., reverse a string) without help?

Yes i can 