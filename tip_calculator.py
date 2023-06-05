# spit buill between number of people input, with percentage input

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $")) # convert string to float
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) # convert string to integer
people = int(input("How many people to split the bill? ")) # convert string to integer

# calculate the tip
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

# calculate the amount per person
bill_per_person = total_bill / people

# format the result to 2 decimal places
final_amount = "{:.2f}".format(bill_per_person)

# print the result
print(f"Each person should pay: ${final_amount}")