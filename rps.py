from random import randint
import random

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
try:
    user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
except ValueError:
    print("Invalid input, please enter a number between 0 and 2")
    exit()

# Validate input
if user_choice not in [0, 1, 2]:
    print("Invalid choice, please choose between 0, 1, and 2.")
    

user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))

computer_choice = random.randint(0,2)
# print(f"computer choice is {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice == computer_choice:
    print("A tie!")
else:
    print("Invalid choice, you lose")