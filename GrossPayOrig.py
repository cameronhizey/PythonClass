hours = input("Enter Hours:")
rate = input("Enter Rate:")
newHours = float(hours)
newRate = float(rate)
output = round(newHours * newRate, 2)
print(f"Pay: {output}")


