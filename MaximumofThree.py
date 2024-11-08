# my attempt

#
# def max_of_three(a, b, c):
#     """Tells highest of three numbers"""
#     if a > b > c or a > c > b:
#         answer = a
#     if b > a > c or b > c > a:
#         answer = b
#     if c > a > b or c > b > a:
#         answer = c
#     if a == b == c:
#         answer = " All numbers are equal."
#     if a == b < c:
#         answer = c
#     if a == c < b:
#         answer = b
#     if c == b < a:
#         answer = a
#     return answer
#
#
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
#
# output = max_of_three(a, b, c)
# print(output)

# guy in videos version
def max_of_two(n1, n2):
    if n1 > n2:
        return n1
    return n2


def max_of_three(n1, n2, n3):
    max_two = max_of_two(n1, n2)
    max_of_three = max_of_two(max_two, n3)
    return max_of_three


print(max_of_three(1, 2, 3))
