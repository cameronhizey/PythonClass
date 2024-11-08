# my attempt
# try:
#    hours = float(input("Enter Hours:\n"))
#    rate = float(input("Enter Rate:\n"))
#    pay = round(hours * rate, 2)
#    if hours <= 40:
#        pay = round(hours * rate, 2)
#        print(f"Pay: {pay}")
#    else:
#        over_time = hours - 40
#        pay = round(rate * 40 + over_time * rate * 1.5, 2)
#        print(f"Pay: {pay}")
# except ValueError:
#    print("Error, please enter numeric input for Rate")
#    quit()

# guy in videos attempt
hour = input("Enter Hours: ")

try:
    hour = float(hour)
except ValueError:
    print("Error, please enter numeric input for Hour")
    quit()

rate = input("Enter Rate: ")

try:
    rate = float(rate)
except ValueError:
    print("Error, please enter numeric input for Rate: ")
    quit()
if hour < 40:
    pay = round(hour * rate, 2)
else:
    overtime = hour - 40
    pay = round(40 * rate + overtime * rate * 1.5, 2)

print(f"Pay: {pay}")
