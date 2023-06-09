# Day 5 of learning Python
# For Loops, Rannge and Code Blocks

# For Loops
# For loops are used to iterate over a sequence (list, tuple, string) or other iterable objects.

# Syntax
# for item in iterable_object:

# list 10 fruitss
fruits = ["Apple", "Peach", "Pear", "Orange", "Banana", "Grape", "Mango", "Pineapple", "Watermelon", "Strawberry"]

for item in fruits:
    print(item)

# For loop with range
# range(start, stop, step)

for number in range(1, 11): # 1 to 10
    print(number)

# range with step
for number in range(1, 11, 3): # 1 to 10 with step 3
    print(number)