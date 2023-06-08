# Day 4 of learning Python
# Randomisation and Python Lists
#
# Building Rock, Paper, Scissors Game
# How Rock, Paper, Scissors works:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
#

import random

random_integer = random.randint(0, 9) # random integer between 0 and 9
random_string = random.choice(["rock", "paper", "scissors"]) # random string from list

# print(random_integer)
# print(random_string)

# building rock, paper, scissors game
# user plays against computer

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice >= 0 and user_choice <= 2:
    options = ["rock", "paper", "scissors"]
    user_choose = options[user_choice]
    computer_choose = options[computer_choice]

    rock = '''
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
    '''

    paper = '''
    _______
---'   ____)____
            ______)
            _______)    
            _______)
---.__________)
    '''

    scissors = '''
    _______
---'   ____)____
            ______)
        __________)
        (____)
---.__(___)
    '''

    symbols = [rock, paper, scissors]

    print(f"You chose:\n{symbols[user_choice]}")
    print(f"Computer chose:\n{symbols[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw.")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
        print("You win!")
    else:
        print("You lose.")
else:
    print("You typed an invalid number. You lose.")