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

# Initializing variables for the player's choice(input) and computer's choice
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if player_choice == 0:
    print("You chose:\n" + rock)
elif player_choice == 1:
    print("You chose:\n" + paper)
elif player_choice == 2:
    print("You chose:\n" + scissors)
com_choice = random.randint(0, 2)
if com_choice == 0:
    print("The computer chose:\n" + rock)
elif com_choice == 1:
    print("The computer chose:\n" + paper)
elif com_choice == 2:
    print("The computer chose:\n" + scissors)

# Conditional statements to compare the player's choice to the computer's choice
# If player chooses Rock(0)
if player_choice == 0:
    if com_choice == 0:
        print("It's a draw.")
    elif com_choice == 1:
        print("You lose...")
    elif com_choice == 2:
        print("You win!!!")
# If player chooses Paper(1)
elif player_choice == 1:
    if com_choice == 0:
        print("You win!!!")
    elif com_choice == 1:
        print("It's a draw")
    elif com_choice == 2:
        print("You lose...")
# If player chooses Scissors(2)
elif player_choice == 2:
    if com_choice == 0:
        print("You lose...")
    elif com_choice == 1:
        print("You win!!!")
    elif com_choice == 2:
        print("It's a draw")
# If player enters number != to 0, 1, or 2
elif player_choice >= 3 or player_choice < 0:
    print("Invalid entry. You lose.")






