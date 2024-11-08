hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
if hours > 40:
    overtime = hours - 40
    overrate = rate * 1.5
    output = (40 * rate) + (overtime * overrate)
    print(f"Pay {output}")
else:
    output = round(hours * rate, 2)
    print(f"Pay: {output}")


'''hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
hour = float(hour)
rate = float(rate)

pay = round(hour*rate, 2)
print(f"Pay: {pay}")'''

#other evolution
hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
hour = float(hour)
rate = float(rate)
if hour < 40:
    pay = round(hour * rate, 2)
else:
    overtime = hour - 40
    pay = round(40 * rate + overtime * rate * 1.5, 2)


print(f"Pay: {pay}")