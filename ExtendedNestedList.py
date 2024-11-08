list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'],'m', 'n']
list1[2][1][2].extend('h')
list1[2][1][2].extend('i')
list1[2][1][2].extend('j')
print(list1)

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'],'m', 'n']
list2 = ['h', 'i', 'j']
list1[2][1][2].extend(list2)
print(list1)
