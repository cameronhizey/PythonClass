# what i did. loops not allowed
dict1 = {'One': 2, 'Two': 2, 'Three': 3}
dict2 = {'Three': 3, 'Four': 4, 'Five': 5}


def merg_dict(p1, p2):
    new_dict = {}
    new_dict.update(p1)
    new_dict.update(p2)
    return new_dict


print(merg_dict(dict1, dict2))

# What guy in video did
def merg_dict(p_dict1, p_dict2):
    dict3 = p_dict1.copy()
    dict3.update(p_dict2)
    return dict3
print(merg_dict(dict1, dict2))