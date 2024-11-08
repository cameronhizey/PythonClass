# what i did
# import random
#
# user_choice = input("Enter a choice (rock, paper, scissors): ")
# play_again = "Y"
# options = "rps"
# computer_option = random.choice(options)
#
# while play_again == "Y":
#     if user_choice == 'rock' and computer_option == 's':
#         print("You selected rock and computer selected scissors. You win!")
#         play_again = input("Play again (Y/N?): ")
#     if user_choice == 'rock' and computer_option == 'p':
#         print("You selected rock and computer selected paper. You lose!")
#         play_again = input("Play again (Y/N?): ")
#     if user_choice == 'rock' and computer_option == 'r':
#         print("You selected rock and computer selected rock. It's a tie!")
#         play_again = input("Play again (Y/N?): ")
#     if user_choice == 'scissors' and computer_option == 'p':
#         print("You selected scissors and computer selected paper. You win!")
#         play_again = input("Play again (Y/N?): ")
#     if user_choice == 'scissors' and computer_option == 'r':
#         print("You selected scissors and computer selected rock. You lose!")
#         play_again = input("Play again (Y/N?): ")
#     if user_choice == 'scissors' and computer_option == 's':
#         print("You selected rock and computer selected rock. It's a tie!")
#         play_again = input("Play again (Y/N?): ")
#     if user_choice == 'paper' and computer_option == 'r':
#         print("You selected rock and computer selected rock. You win!")
#         play_again = input("Play again (Y/N?): ")
#     if user_choice == 'paper' and computer_option == 's':
#         print("You selected rock and computer selected paper. You lose!")
#         play_again = input("Play again (Y/N?): ")
#     if user_choice == 'paper' and computer_option == 'p':
#         print("You selected rock and computer selected rock. It's a tie!")
#         play_again = input("Play again (Y/N?): ")

# What guy on video did
import random


def select_computer_action():
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_action)
    return computer_action


def determine_winner(p_computer_action, p_user_action):
    if p_user_action == p_computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif p_user_action == "rock":
        if p_computer_action == "scissors":
            print("Rock smashes scissors! You Win!")
        else:
            print("Paper covers rock! You lose.")
    elif p_user_action == "paper":
        if p_computer_action == "rock":
            print("paper covers rock! You Win!")
        else:
            print("Paper is cut by scissors. You lose.")
    elif p_user_action == "scissors":
        if p_computer_action == "paper":
            print("scissors cuts paper! You Win!")
        else:
            print("scissors is smashed by rock! You lose.")


while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    computer_action = select_computer_action()
    print(f"\nYou chose {user_action}, computer chose {computer_action}")
    determine_winner(computer_action, user_action)
    play_again = input("play again (Y/N)?")
    if play_again != "Y":
        break
