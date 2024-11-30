# Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the
# alphabet at least once. For example: "The quick brown fox jumps over the
# lazy dog"

import string

def is_pangram(sentence):
  
    alphabet_set = set(string.ascii_lowercase)
    
    sentence_set = set(char.lower() for char in sentence if char.isalpha())
    
    return alphabet_set.issubset(sentence_set)

user_input = input("Enter a sentence to check if it's a pangram: ")

if is_pangram(user_input):
    print(f'"{user_input}" is a pangram!')
else:
    print(f'"{user_input}" is not a pangram.')
