
# 2. Write a Python function that checks whether a word or phrase is palindrome or
# not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"

def is_palindrome(text):
   
    text = ''.join(char.lower() for char in text if char.isalnum())

    return text == text[::-1]

user_input = input("Enter a word or phrase to check if it's a palindrome: ")

if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome!')
else:
    print(f'"{user_input}" is not a palindrome.')
