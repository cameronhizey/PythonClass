print("Welcome to Mortgage Calculator")
salary = int(input("What is your salary? "))

if salary >= 2000:
    print("You are eligible for mortgage!")
    credit_score = int(input("What is your credit score? "))
    if credit_score > 800:
        print("Interest rate 4%")
    elif credit_score > 750:
        print("Interest rate: 6%")
    else:
        print("Interest rate: 8%")
else:
    print("sorry, you are not eligible!")



# chained conditional with multiple if statements
print("Welcome to Mortgage Calculator")
salary = int(input("What is your salary? "))
rate = 0


if salary >= 2000:
    print("You are eligible for mortgage!")
    credit_score = int(input("What is your credit score? "))
    if credit_score > 800:
        rate = 4
        print("Interest rate 4%")
    elif credit_score > 750:
        rate = 6
        print("Interest rate: 6%")
    else:
        rate = 8
        print("Interest rate: 8%")
    disability = input("Do you have any disability? Y or N:")
    if disability == "Y":
        rate -= 2
    print(f"Final Interest Rate: {rate}")
else:
    print("sorry, you are not eligible!")