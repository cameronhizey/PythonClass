#wHAT I did
# import random
#
# letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# nums = '1234567890'
# symbols = '-+=!@#$%^&*'
# new_letters = ""
# new_nums = ""
# new_symbols = ""
#
# letter_total = int(input("How many letters do you want in your password? "))
# nums_total = int(input("How many numbers do you want in your password? "))
# symbols_total = int(input("How many symbols do you want in your password? "))
#
# while letter_total > 0:
#     new_letter = random.choice(letters)
#     new_letters += new_letter
#     letter_total -= 1
# while nums_total > 0:
#     new_num = random.choice(nums)
#     new_nums += new_num
#     nums_total -= 1
# while symbols_total > 0:
#     new_symbol = random.choice(symbols)
#     new_symbols += new_symbol
#     symbols_total -= 1
#
# new_password = (new_letters + new_nums + new_symbols)
#
# print(new_password)

#What guy in video did
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

number_of_letters = input("How many letters do you want in your password? ")
number_of_nums = input("How many numbers do you want in your password? ")
number_of_symbols = input("How many symbols do you want in your password? ")

number_of_letters = int(number_of_letters)
number_of_nums = int(number_of_nums)
number_of_symbols = int(number_of_symbols)
password = ""

for letter in range(1, number_of_letters + 1):
    password += random.choice(letters)

for num in range(1, number_of_nums + 1):
    password += random.choice(nums)

for symbol in range(1, number_of_symbols + 1):
    password += random.choice(symbols)

#add on not apart of initial task
password_list = list(password)
random.shuffle(password_list)

advanced_password = ""
for apc in password_list:
    advanced_password += apc

print(f"Your password is: {advanced_password}")
