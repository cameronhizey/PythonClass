#What i did
num_list = range(101)
for numbers in num_list:
    if numbers % 5 == 0 and numbers % 7 == 0:
        print("FizzBuzz")
    elif numbers % 5 == 0:
        print("Fizz")
    elif numbers % 7 == 0:
        print("Buzz")
    else:
        print(numbers)

#Guy in video did same thing.