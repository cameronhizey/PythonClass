# first attempt
# first_number = int(input("What is the first number?"))
# second_number = int(input("What is the second number?"))
# operation = input("Which operation do you want +,-,*,/?")
# if operation == "+":
#     result = first_number + second_number
#     print(result)
# elif operation == "-":
#     result = first_number - second_number
#     print(result)
# elif operation == "*":
#     result = first_number * second_number
#     print(result)
# elif operation == "/":
#     result = first_number / second_number
#     print(result)
# else:
#     print("Invalid operation")

# second attempt
# def add(n1, n2):
#     result = n1 + n2
#     return result
#
#
# def subtract(n1, n2):
#     result = n1 - n2
#     return result
#
#
# def multiply(n1, n2):
#     result = n1 * n2
#     return result
#
#
# def division(n1, n2):
#     result = n1 / n2
#     return result
#
#
# first_number = int(input("What is first number? "))
# second_number = int(input("What is second number? "))
# operation = input("Pick operation from this list (+,-,*,/)")
#
# if operation == "+":
#     result = add(n1=first_number, n2=second_number)
#     print(f"{first_number} + {second_number} = {result}")
# elif operation == "-":
#     result = subtract(n1=first_number, n2=second_number)
#     print(f"{first_number} - {second_number} = {result}")
# elif operation == "*":
#     result = multiply(n1=first_number, n2=second_number)
#     print(f"{first_number} * {second_number} = {result}")
# elif operation == "/":
#     result = division(n1=first_number, n2=second_number)
#     print(f"{first_number} / {second_number} = {result}")


# What guy in video did
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


n1 = int(input("What is first number? "))
n2 = int(input("What is second number? "))
operation = input("Pick operation from this list (+,-,*,/) ")

if operation == "+":
    answer = add(n1, n2)
elif operation == "-":
    answer = subtract(n1, n2)
elif operation == "*":
    answer = multiply(n1, n2)
elif operation == "/":
    answer = divide(n1, n2)

print(f"{n1} {operation} {n2} = {answer}")
