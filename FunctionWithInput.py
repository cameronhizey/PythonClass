def greet():
    print("Hello")
    print("How are you?")


greet()


# Function with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}")


greet_with_name("Eddy")

def greet_withNC(name, city):
    print(f"hello {name}")
    print(f"what is the weather like in {city}")

greet_withNC("Cameron", "Madison")

def area_of_square(side):
    area = side * side
    print(area)


area_of_square(6)


def area_of_square(side):
    area = side * side
    print(area)

area_of_square(6)
