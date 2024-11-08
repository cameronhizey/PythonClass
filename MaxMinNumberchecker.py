def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, please enter numeric input")
        return False


num_list = []
max_num = 0
min_num = 0
while True:
    input_number = input("Enter a number: ")
    if input_number == "done":
        break

    number = check_for_float(input_number)
    if not number:
        continue

    num_list.append(number)
    max_num = max(num_list)
    min_num = min(num_list)

print(f"Maximum number: {max_num}, Minimum number: {min_num}")


# What i did:
# def check_for_float(p_input):
#     try:
#         val = float(p_input)
#         return val
#     except (ValueError, TypeError):
#         print("Error, please enter numeric input")
#         return False
#
#
# num_list = []
# max_num = "No number entered"
# min_num = "No number entered"
# while True:
#     input_number = input("Enter a number: ")
#     if input_number == "done":
#         break
#
#     number = check_for_float(input_number)
#     if not number:
#         continue
#
#     num_list.append(number)
#     max_num = max(num_list)
#     min_num = min(num_list)
#
# if max_num and min_num == "No number entered":
#     print("No Number entered")
# else:
#     print(f"Maximum number: {max_num}, Minimum number: {min_num}")


# What guy in video did

def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, please enter numeric input")
        return False


input1 = input("Enter a number: ")
if input1 == "done":
    quit()
number = check_for_float(input1)
if not number:
    print("The first entered has to be number to continue.")
    quit()

smallest = number
biggest = number

while True:
    input1 = input("Enter a number: ")
    if input1 == "done":
        break

    number = check_for_float(input1)
    if number > biggest:
        biggest = number
    if number < smallest:
        smallest = number
        continue

print(f"Maximum number: {biggest}, Minimum number: {smallest}")
