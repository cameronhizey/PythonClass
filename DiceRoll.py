# WHAT I DID
# import random
#
# diceone = random.randint(1, 6)
# dicetwo = random.randint(1, 6)
# print(f"Dice1: {diceone}\nDice2: {dicetwo}")
#
# while True:
#     action = input("Roll dice again? (Y/N)")
#     if action == "N":
#         quit()
#     if action == "Y":
#         diceone = random.randint(1, 6)
#         dicetwo = random.randint(1, 6)
#         print(f"Dice1: {diceone}\nDice2: {dicetwo}")
#     else:
#         print('Please Enter Y/N')

# What guy in video did
import random

roll_again = "Y"
while roll_again == "Y":
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice1: {dice1}", f"\nDice2: {dice2}")
    roll_again = input("Roll the dice again? (Y/N ")
