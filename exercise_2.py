# BMI

# Instructions
#  If BMI is less than 18.5, they are underweight.
#  If BMI is between 18.5 and 25, they have a normal weight.
#  If BMI is between 25 and 30, they are slightly overweight.
#  If BMI is between 30 and 35, they are obese.
#  If BMI is greater than 35, they are clinically obese.

# Solution 
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# bmi = weight / height ** 2 

bmi= round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# Solution 2
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
    