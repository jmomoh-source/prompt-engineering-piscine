import re

def isPalindrome(s):
    s_clean = re.sub(r'[^a-z0-9]', '', s.lower())

    if s == s[::-1]:
        print("Yes")
    else:
        print("No")

    # Test different cases directly:
print("Testing empty string:")
isPalindrome("")

print("Testing with punctuation:")
isPalindrome("Was it a car or a cat I saw?")

print("Testing normal:")
isPalindrome("racecar")

word = input ("enter your string: ")
isPalindrome(word)


def palindrome(text):

    // Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    
    // Check if the cleaned text is a palindrome

    for i in range(len(cleaned_text) // 2):
        
        // Compare characters from the start and end
        if cleaned_text[i] != cleaned_text[len(cleaned_text) - 1 - i]:
            return i  # Position where it fails
    
    // If we reach here, it's a palindrome
    return True  # It's a palindrome