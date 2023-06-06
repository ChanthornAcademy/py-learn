# Instructions
# Write a program that determines if a number is odd or even. 
# An even number is divisible by 2 with no remainder. 
# If a number is odd, it will have a remainder when divided by 2. 
# Use the modulo operator (%) to find the remainder. 
# If the remainder is 0, the number is even. 
# If the remainder is 1, the number is odd. 
# The program should output "This is an odd number." or "This is an even number."
#  depending on the input.

# Example Input 1
# 43
# Example Output 1
# This is an odd number.
# Example Input 2
# 94
# Example Output 2
# This is an even number.

# Solution
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Solution 2
if number % 2 != 0:
    print("This is an odd number.")
else:
    print("This is an even number.")