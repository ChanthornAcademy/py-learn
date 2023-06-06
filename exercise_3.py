# Leap Year
# What is a leap year?
# - on every year that is evenly divisible by 4
# - except every year that is evenly divisible by 100
# - unless the year is also evenly divisible by 400
#
# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
#
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)
# Write a program that works out whether if a given year is a leap year.

# Solution
year = int(input("Which year do you want to check? "))
is_leap = False
# use nested if / else
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            # print("Leap year.")
            is_leap = True
        else:
            # print("Not leap year.")
            is_leap = False
    else:
        # print("Leap year.")
        is_leap = True
else:
    # print("Not leap year.")
    is_leap = False


# use if / else
print("Result from solution 1")
if is_leap:
    print("Leap year.")
else:
    print("Not leap year.")


# Solution 2 with Logical Operators (and, or, not)
if(year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    # print("Leap year.")
    is_leap = True
else:
    # print("Not leap year.")
    is_leap = False

# use if / else
print("Result from solution 2")
if is_leap:
    print("Leap year.")
else:
    print("Not leap year.")

