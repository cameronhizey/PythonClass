# First attempt without looking at instructions

# import random
#
# try:
#     guessRemain = 1
#     lowerBound = int(input("Enter Lower Bound number"))
#     upperBound = int(input("Enter upper bound number"))
#     bounds = random.randint(lowerBound, upperBound)
#     if upperBound <= lowerBound:
#         print('Lower bound must be lower than upper bound.')
#     guess1 = int(input("Enter first guess: "))
#     if guess1 == bounds:
#         print(f"Congratulations you did it in {guessRemain}")
#         quit()
#     elif guess1 > bounds:
#         print("You guessed too high.")
#     else:
#         print("You guessed too low.")
#     guessRemain = 2
#     guess2 = int(input("Enter first guess: "))
#     if guess2 == bounds:
#         print(f"Congratulations you did it in {guessRemain}")
#         quit()
#     elif guess2 > bounds:
#         print("You guessed too high.")
#     else:
#         print("You guessed too low.")
#     guessRemain = 3
#     guess3 = int(input("Enter first guess: "))
#     if guess3 == bounds:
#         print(f"Congratulations you did it in {guessRemain}")
#         quit()
#     elif guess3 > bounds:
#         print("You guessed too high.")
#     else:
#         print("You guessed too low.")
#     print("Sorry you did not guess the number")
#
# except (ValueError, TypeError):
#     print("Must enter numeric number")


# second attempt after looking at instructions

# import math
# import random
#
# try:
#     lowerBound = int(input("Enter Lower Bound number: "))
#     upperBound = int(input("Enter upper bound number: "))
#     answer = random.randint(lowerBound, upperBound)
#     chances = round(math.log(upperBound - lowerBound + 1, 2))
#     guesses = 0
#     if upperBound <= lowerBound:
#         print('Lower bound must be lower than upper bound.')
#     print(f"\n\tYou've only {chances} chances to guess the integer!\n")
#     while chances > 0:
#         guess = int(input("Enter guess: "))
#         if guess == answer:
#             guesses += 1
#             print(f"Congratulations you did it in {guesses}\n The number is {answer}")
#             break
#         elif guess > answer:
#             guesses += 1
#             print("You guessed too high.")
#             chances -= 1
#         else:
#             guesses += 1
#             print("You guessed too low.")
#             chances -= 1
#     if chances == 0:
#         print(f"The number is {answer}\n\tBetter Luck Next Time")
#
# except (ValueError, TypeError):
#     print("Must enter numeric number")

# what guy in video did

import math
import random

lower = int(input("Enter Lower Bound: "))
upper = int(input("Enter Upper Bound: "))
number_of_chances = int(math.log(upper - lower + 1, 2))
print(f"\n\tYou've only {number_of_chances} chances to gues the integer!\n")

generated_number = random.randint(lower, upper)

count = 0
while count < number_of_chances:
    count += 1
    guess = int(input("Guess a number: "))
    if generated_number == guess:
        print(f"Congratulations you did it in {count} try")
        break
    elif guess > generated_number:
        print("You guessed too high!")
    elif guess < generated_number:
        print("You guessed too low!")
print(f"\nThe number is {generated_number} ")
print("\tBetter Luck Next Time.")
