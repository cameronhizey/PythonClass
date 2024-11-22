names_dict = {
    1 : "Elshad",
    2 : "Renad",
    3 : "Johanna",
    4 : "Appmillers"
}

def value_length(p_dict):
    new_dict = {}
    for item, value in p_dict.items():
        new_dict[item] = {}
        new_dict[item][value] = len(value)


    return new_dict

print(value_length(names_dict))


