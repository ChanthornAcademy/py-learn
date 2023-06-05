# Day 2 of learning Python
# Learning about variables and data types: strings, integers, floats, booleans

country = "Cambodia" # string
city = "Phnom Penh" # string
isTrue = True # boolean
isFalse = False # boolean
age = 20 # integer
height = 1.75 # float
print("I am from " + country + " and I live in " + city)
print("I am " + str(age) + " years old and I am " + str(height) + " meters tall")

# get first letter of string
print(country[0])

# get first 3 letters of string 0= start, 3 = end
print(country[0:3])

# check type of variable
print('Check type of variable')
print(type(country))
print(type(age))
print(type(height))
print(type(isTrue))
print(type(isFalse))

# casting variables
print('Casting variables')
print(int(height)) # convert float to integer
print(float(age)) # convert integer to float
print(str(isTrue)) # convert boolean to string
print(bool(age)) # convert integer to boolean

# PENDASLR
print((3*2)+(3/3)-4) # 3*2+1-4 = 3*2-3 = 6-3 = 3


# Math operations: +, -, *, /, %, **, //
# Calculator program using user input
print("Calculator")
num1 = input("Enter first number: ")
# input operator
operator = input("Enter operator: ")
num2 = input("Enter second number: ")

# convert string to integer
# convert num1 and num2 from string to integer
num1 = int(num1)
num2 = int(num2)

# check the operator and perform the corresponding operation
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "%":
    print(num1 % num2)
elif operator == "**":
    print(num1 ** num2)
elif operator == "//":
    print(num1 // num2)
else:
    print("Invalid operator")

