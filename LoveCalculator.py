# my attempt b4 video
# print("Welcome to Love Calculator!")
# name1 = input("What is the first lovers name?")
# name2 = input('What is the second lovers name?')
# true = "'t', 'r', 'u', 'e'"
# love = "'l', 'o', 'v', 'e'"
# first = (name1.lower())
# second = (name2.lower())
# counts = (first.count(true))
# print(counts)
#

# His version
print("Welcome to Love Calculator!")
name1 = input("Enter your name: ")
name2 = input("Enter your lovers name: ")

combined_name = name1 + name2
lower_case_name = combined_name.lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
if love_score < 10 or love_score > 85:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 70:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}.")