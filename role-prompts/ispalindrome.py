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