# What i did
def sum_of_two_digits():
    two_digits = input("Enter two digit number: ")
    first_digit = two_digits[0:1]
    first_digit = int(first_digit)
    second_digit = two_digits[1:2]
    second_digit = int(second_digit)
    answer = first_digit + second_digit
    return answer


# what guy in video did
def sum_of_two_digits():
    two_digit_number = input("Enter two digit number: ")
    sum_of_digits = int(two_digit_number[0]) + int(two_digit_number[1])
    return sum_of_digits


print(sum_of_two_digits())
