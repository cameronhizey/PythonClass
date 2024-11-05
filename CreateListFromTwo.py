list_one = [4, 12, 16, 21, 24, 28, 32]
list_two = [5, 10, 15, 20, 25, 30, 35]
list_three = []
l = len(list_one)
i = 0
for nums in list_one:
    if nums != list_one[i]:
        list_three.append(nums)
        i+=2

i = 0
for nums in list_two:
    if nums == list_two[i]:
        list_three.append(nums)
        i+=2
print(list_three)