# How I did it

# def temperature_input(t1):
#     if t1 < 18:
#         answer = "cold"
#     elif 18 <= t1 <= 28:
#         answer = "warm"
#     elif t1 > 28:
#         answer = "Hot"
#     return answer
#
#
# temperature = int(input("What is the temperature? "))
#
# output = temperature_input(temperature)
#
# print(output)


# How guy in video did it
def check_temp(temp):
    if temp > 28:
        return "Cold"
    elif temp >= 18 and temp <= 28:
        return "Warm"
    else:
        return "Cold"


temp = int(input("Enter temperature: "))
print(check_temp(temp))
