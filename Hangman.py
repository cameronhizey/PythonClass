# import random
# word_list = ["UDEMY", "APPMILLERS", "PYTHON"]
#
# select = random.randint(0, 2)
# secret_word = word_list[select]
# secret_len = len(secret_word)
# space = []
# for _ in secret_word:
#     blank = "_"
#     space.append(blank)
#
# guess = input("Guess a letter: ").upper()
#
# guessed_letter = []
# def guess_checker(p_guess):
#     if p_guess in guessed_letter == True:
#         print("Already guessed, try again")
#     else:
#         guessed_letter.append(guess)
#
#
# print(secret_word.index(guess))
# def letter_checker(p_check):
#     if p_check in secret_word:
#         space.insert(i, p_check):
#         if guess in secret_word:
#             space[i].replace(guess)

import random
word_list = ["APPMILLERS", "UDEMY"]
secret_word = random.choice(word_list)
word_length = len(secret_word)
guessed_letters = []
blanks = []
lives = 6
for _ in range(word_length):
    blanks.append("_")
end_game = False
while not end_game:
    guess = input("Guess a letter: ").upper()
    if guess in guessed_letters:
        print("You have already guessed this letter!")
        continue
    else:
        guessed_letters.append(guess)

    for position in range(word_length):
        letter = secret_word[position]
        if guess == letter:
            blanks[position] = letter
    if guess not in secret_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Lose.")

    print(" ".join(blanks))
    print(lives)
    if "_" not in blanks:
        end_game = True
        print("You win")
    if end_game:
        ask = input("Do you want to play again?(Y/N) ")
        if ask == "Y":
            secret_word = random.choice(word_list)
            blanks.clear()
            word_length = len(secret_word)
            for _ in range(word_length):
                blanks.append("_")
            end_game = False
            guessed_letters.clear()
            lives = 6
        else:
            print("See you next time.")