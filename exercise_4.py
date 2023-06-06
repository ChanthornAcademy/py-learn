# Pizza Order 
# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill.
#
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Solution
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# covert size to uppercase if user input lowercase
size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()
bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2 # +=2 is the same as bill = bill + 2 (add 2 to bill / បូកថែម២នៅលើ bill)
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
elif size == "S" or size == "M" or size == "L":
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
else:
    print("Please enter valid input.")