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
game_images = [rock, paper, scissors]

import random
user_choice = int(input("what do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
    exit()
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer is Choosen:\n{game_images[computer_choice]}")


# Three Basic rules of RPS
#1. Rock wins against scissors
#2. Scissors win against paper
#3. Paper wins against rock


if user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")