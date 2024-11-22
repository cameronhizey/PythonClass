# what i did
# import copy
original_dict = {
    "names": ["Elshad", "John", "Edy"],
    "numbers": [1, 2, 3, 4, 5]
}
#
# def deep_copy(p_dict, p_name, p_num):
#     copied_dict = copy.deepcopy(p_dict)
#     copied_dict["names"].append(p_name)
#     copied_dict["numbers"].append(p_num)
#     return copied_dict
#
# print(original_dict)
# print(deep_copy(original_dict, "jack", 6))

# what guy in video did
def deep_copy(p_dict):
    new_dict = {}
    for key, value in p_dict.items():
        new_value = value.copy()
        new_dict[key] = new_value
    return new_dict

copied_dict = deep_copy(original_dict)
copied_dict["names"].append("Jack")
copied_dict["numbers"].append(6)
print(original_dict)
print(copied_dict)