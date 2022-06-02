#images for rock, paper, scissors
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

#import packages
import random

#store image in list
game_images= [rock,paper,scissors]

#assign variable to player input
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

#catching invalid inputs first
if player >= 3 or player < 0:
  print("You typed an invalid number")
else:
  print(game_images[player])
#randdom computer input
  computer = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer])

#rules for winning/losing
  if player == computer:
    print("Its a draw.")
  elif player == 0 and computer == 2:
    print("You win")
  elif computer == 0 and player == 2:
    print("You lose")
  elif computer > player:
    print("You lose")
  elif computer < player:
    print("You win")
