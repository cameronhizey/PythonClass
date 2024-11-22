dict1={1: "one", 2: "two"}
dict2={3: "three", 4: "four"}
dict3={5: "five", 6: "six"}
# what i did

def concatenate(p1, p2, p3):
    new_dict = {}
    new_dict.update(p1)
    new_dict.update(p2)
    new_dict.update(p3)
    return new_dict

print(concatenate(dict1, dict2, dict3))

# what guy in video did

def concatenate(d1, d2, d3):
    new_dict = {}
    for dic in [d1, d2, d3]:
        new_dict.update(dic)
    return new_dict

