# def palindrome(text):
#     cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    
# # Loop through and find mismatch position
#     for i in range(len(cleaned_text) // 2):

# # Compare position i with its mirror position
#         if cleaned_text[i] != cleaned_text[len(cleaned_text) - 1 - i]:
#             return i
    
#     return True 

# word = input ("enter your text: ")

# print("palindrome" if palindrome(word) else "it is not palindrome")
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
