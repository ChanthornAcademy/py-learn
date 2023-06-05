# This code calculates how many days, weeks, and months are left until you turn 90 years old.
# It then prints the results.

age = input('What is your current age? ')
# covert string to integer
age = int(age)
# calculate the number of days, weeks, and months left until 90 years old
weeks_per_year = 52
days_per_year = 365
months_per_year = 12
years_left = 90 - age
days_left = years_left * days_per_year
weeks_left = years_left * weeks_per_year
months_left = years_left * months_per_year
# print the result
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")