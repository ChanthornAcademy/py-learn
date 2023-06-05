heigh = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# convert string to float
heigh = float(heigh)
weight = float(weight)

# BMI = weight(kg) / height(m)^2
bmi = weight / (heigh ** 2)


bmi_int = int(bmi)

print(round(bmi, 2))
print(bmi_int)
print(f"Your BMI is {bmi_int}")


