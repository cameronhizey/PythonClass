# my attempt
# import math


# def wall_size(height, width, ):
#     area = height * width
#     result = math.ceil(area / 4)
#     print(f"{result} cans are needed")
#
#
# wall_size(height=5, width=2)

# what guy did
import math


def calculate_can_number(height, width, coverage):
    area = height * width
    number_of_cans = math.ceil(area / coverage)
    print(number_of_cans)


height = int(input("Enter height of wall: "))
width = int(input("Enter width of wall: "))

calculate_can_number(height, width, 4)
