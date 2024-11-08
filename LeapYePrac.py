# how I solved this
print("Welcome to Leap Year calculator.")
year = int(input("What year is it?"))
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"{year} is A leap year")
elif year % 4 == 0 and year % 100 > 0:
    print(f"{year} is A leap year")
else:
    print(f"{year} is not A leap year")


# How guy in video solved this
year = int(input("Enter year: "))
if year % 4 ==0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


year = int(input("Enter Year: "))
if year % 4 == 0:
    newYear = year
    if newYear % 100  == 0:
        if newYear % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap year")
    else:
        print("Leap Year")
else:
    print("Not leap year")