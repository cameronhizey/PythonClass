names = ['John', 'Edy', 'Jane', 'Kane']
scores = [90, 95, 80, 75]
namelist = len(names)
n = 0
txt = "{}{:^10}"
print(txt.format)
while n < namelist:
    name = names[n]
    score = scores[n]
    print(txt.format(name, score))
    n += 1

