# This code takes a two digit number and adds the digits together.
# two_digit_number is a string that the user inputs
# first_digit is the first digit of the two digit number
# second_digit is the second digit of the two digit number
# two_digit_number is the sum of the first and second digit

two_digit_number = input("Type a two digit number: ")


# check if the number is two digits
if len(two_digit_number) != 2:
    print("Please enter a two digit number")
else:
    #Get the first and second digits using subscripting then convert string to int.
    first_digit = int(two_digit_number[0])
    second_digit = int(two_digit_number[1])
    #Add the two digits togeter
    two_digit_number = first_digit + second_digit
    print(f"Your number is {two_digit_number}")

