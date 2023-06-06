# Nested if / else

# Draw a flowchart for this program:
# [Start] --> (Condition A) --> |Yes| --> (Condition B) --> |Yes| --> (Action 1) --> [End]
        #  |                     |No
        #  |                     v
        #  |--> (Action 2) --> (Condition C) --> |Yes| --> (Action 3) --> [End]
                                            #   |No
                                            #   v
                                            #   (Action 4) --> [End]

print("Welcome to the rollercoaster!")
hieght = int(input("What is your height in cm? "))

if hieght >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
