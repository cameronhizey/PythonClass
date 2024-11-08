# my attempt
# print("Yo Yo Yo Welcome to Dad Burger")
# order = input("Would you like a Mini, Normal or Large burger?")
# size = len(order)
# 4 = mini, 6 = normal, 5 = large
# add_mushroom = input("Would you like to add mushrooms? Yes or No")
# mushrooms = len(add_mushroom)
# yes = 3 no = 2
# add_cheese = input("Would you like cheese with that? Yes or No")
# cheese = len(add_cheese)
# Yes = 3, No = 2
# if size == 4:


# What the guy in the video did
print("Welcome to Burger Shop!")
size = input("What size Burger do you want? M, N, or L")
add_mushroom = input("Do you want mushroom? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0

if size == "M":
    bill += 5
elif size == "N":
    bill += 8
elif size == "L":
    bill += 10

if add_mushroom == "Y":
    if size == "L":
        bill += 2
    else:
        bill += 1

if extra_cheese == "Y":
    bill += 1

print(f'Your final bill is: {bill}')
