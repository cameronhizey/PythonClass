# What i did
# leap year with function solution
# year = int(input("Enter year: "))
#
# def leap_year(year):
#     ly = True
#     nly = False
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return ly
#             else:
#                 return nly
#         else:
#             return ly
#     else:
#         return nly
#
#
# if leap_year(year) == True:
#     print("Leap year")
# else:
#     print("Not leap year")
#
# What guy in video did

import leap

year = int(input("Enter year: "))


print(leap.leap_year(year))
