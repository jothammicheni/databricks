# 5. Write a program that accepts a string as input, capitalizes the first letter of each
# word in the string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

def capitalize_words(input_string):

    return input_string.title()

user_input = input("Enter a string: ")

result = capitalize_words(user_input)
print(f'The capitalized string is: "{result}"')
