list1 = [1,2,3,4,5]
def custom_insert(p_list, num):
    p_list2 = []
    p_list2.extend(p_list)
    l = len(p_list2)
    p_list2.insert(l, num)
    return p_list2
list2 = custom_insert(list1, 6)
print(list1)
print(list2)



# list1 = [1,2,3,4,5]
# l = len(list1)
# list1.insert(l, 6)
# print(list1)
# print(list2)