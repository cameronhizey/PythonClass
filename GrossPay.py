# hour = input("Enter Hours: ")
#
# try:
#     hour = float(hour)
# except ValueError:
#     print("Error, please enter numeric input for Hour")
#     quit()
#
# rate = input("Enter Rate: ")
#
# try:
#     rate = float(rate)
# except ValueError:
#     print("Error, please enter numeric input for Rate: ")
#     quit()
# if hour < 40:
#     pay = round(hour * rate, 2)
# else:
#     overtime = hour - 40
#     pay = round(40 * rate + overtime * rate * 1.5, 2)
#
# print(f"Pay: {pay}")


def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except ValueError:
        print("Error, please enter a numeric input for hours")
        quit()



def compute_pay(p_hour, p_rate):
    if p_hour < 40:
        pay = round(p_hour * p_rate, 2)
    else:
        overtime = p_hour - 40
        pay = round(40 * p_rate + overtime * p_rate * 1.5, 2)
    return pay



hour = input("Enter Hours: ")
hour = check_for_float(hour)
rate = input("Enter rate: ")
rate = check_for_float(rate)

output = compute_pay(hour, rate)


print(output)

