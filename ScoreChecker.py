# my attempt
#try:
#    grade = float(input("Enter score: "))
#except:
#    print("Bad score")
#    quit()
#else:
#    if grade >= 0.9 and grade <= 1:
#        print("A")
#    elif grade >= 0.8 and grade < 9:
#        print("B")
#    elif grade >= 0.7 and grade < 8:
#        print("C")
#    elif grade >= 0.6 and grade < 7:
#        print("D")
#    elif grade < 0.6:
#        print("F")
#    else:
#        print("Bad score")

# what guy in video did kinda
score = input("Enter score: ")

try:
    score = float(score)
except ValueError:
    print("bad score")
    quit()

if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        print("A")
    if score >= 0.8:
        print("B")
    if score >= 0.7:
        print("C")
    if score >= 0.6:
        print("D")
    if score >= 0.0:
        print("F")
else:
    print("Bad score")