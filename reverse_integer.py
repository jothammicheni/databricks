# 4. Write a program that takes an integer as input and returns an integer with
# reversed digit ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19

def reverse_integer(number):   
    reversed_str = str(abs(number))[::-1]

    reversed_number = int(reversed_str)

    if number < 0:
        reversed_number = -reversed_number
    
    return reversed_number

user_input = int(input("Enter an integer: "))

result = reverse_integer(user_input)
print(f"The reversed integer is: {result}")
