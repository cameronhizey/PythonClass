custom_dict = {
    "name" : "Elshad",
    "age" : 28,
    "city" : None
}
# What i did
# def remove_empty_items(p_dict):
#     new_dict = {}
#     for item, value in p_dict.items():
#             new_dict[item] = value
#     for item, value in p_dict.items():
#         if value is None:
#             del new_dict[item]
#
#     return new_dict

# print(remove_empty_items(custom_dict))

# What guy in video did
def remove_empty_items(p_dict):
    for key, value in list(p_dict.items()):
        if value is None:
            p_dict.pop(key)
    return p_dict

print(remove_empty_items(custom_dict))