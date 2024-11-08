# What I did
# fruit = input("Enter a string: ")
# index = 0
# len_fruit = len(fruit)
# no_fruit = -1
# while index < len_fruit:
#     print(fruit[no_fruit])
#     index += 1
#     no_fruit -= 1
#
# What guy in video did
new_string = input("Enter a string: ")
index = -1
length = -1 * len(new_string)

while index >= length:
    letter = new_string[index]
    print(letter)
    index -= 1
