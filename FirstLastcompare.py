list1 = ['cbc', 'xyz', 'aba', '2332']

def count_words(p_list):
    total = 0
    for count in p_list:
        if count[0] == count[-1] and len(count) >= 2:
            total += 1
    return total
print(count_words(list1))