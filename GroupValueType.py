# what i did
custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
def group_types(p_list):
    new_dict = {}.fromkeys(p_list)
    for item in p_list:
        if isinstance(item, str):
            new_dict[item] = "string"
        elif isinstance(item, int):
            new_dict[item] = "integer"
    return new_dict

print(group_types(custom_list))