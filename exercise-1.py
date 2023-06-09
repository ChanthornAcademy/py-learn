# Exercise 1 - Average Height
# Instructions
# You are going to write a program that calculates the average staff height from a List of heights.

staff_heights = [180, 124, 165, 173, 189, 169, 146] # cm
# using for loop 
total_height = 0
for height in staff_heights:
    total_height += height

staff_count = 0
for staff in staff_heights:
    staff_count += 1

average_height = round(total_height / staff_count)

print(f"Average height is {average_height} cm.")

# by user input 

staff_heights_input = input("Input staff heights separated by space: ").split(" ")

print(staff_heights_input)

total_height = 0
staff_count = 0
for height in staff_heights_input:
    total_height += int(height)
    staff_count += 1

average_height = round(total_height / staff_count)

print(f"Average height is {average_height} cm.")
