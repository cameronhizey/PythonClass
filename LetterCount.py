# what i did
word_input = input("Enter word")
letter_input = input("Pick a letter from word: ")


def count_letter(word, letter):
    letter_total = 0
    for letter_choice in word:
        if letter_choice == letter:
            letter_total += 1
    return letter_total


print(count_letter(word_input, letter_input))

# what guy in video did

def count_letter(word, letter):
    counter = 0
    for char in word:
        if char == letter:
            counter += 1
    return counter
#
#
# print(count_letter("Learning Python", 'n'))
