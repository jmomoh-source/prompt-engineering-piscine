    Modify your palindrome function to:

    def palindrome(text):
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    
# Loop through and find mismatch position
    for i in range(len(cleaned_text) // 2):

# Compare position i with its mirror position
        if cleaned_text[i] != cleaned_text[len(cleaned_text) - 1 - i]:
            return i
    
    return True 

word = input ("enter your text: ")

print("palindrome" if palindrome(word) else "it is not palindrome")


## After your first attempt, ask AI:
- The Ai brought up th errors in my coe on the "Return the position where the string stops being a palindrome (if not one)." and gave me the steps to solve the problem myself. 

- Did I miss anything? 
Yes The print statement in my code does not use the position number function in my code.
It also pointed the mixed returns can be confusing because of "0" it is also False in python

- Can it be more efficient?"
well my code is already quite efficient, but i could avoid creating cleaned_text and compare while cleaning, but it makes code harder to read for minimal gain.

## Reflect on what AI added that you didn't consider initially.
- Well my first code i wrote was checked more of simple palindrome, and when the task got difficult to handle capitalization and remove spaces.
- AI mentioned the edge cases i missed, pointed out the print statement issue i had not printing the position number and the bolean result, and the result type problem with "False" and "0".
Suggested a better approach like the two-pointer.
- I was quite surprised from the feedback because i thought i had sorted my print statement code correctly until i was shown. next time i would do more testing in terms of edge cases, and think about th return values more carefully.