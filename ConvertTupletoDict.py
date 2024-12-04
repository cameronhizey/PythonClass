tuple_list = [("one", 1), ("two", 2), ("three", 3), ("four", 4)]


def convert_to_dict(p_tuple):
    new_dict = {}
    for items in p_tuple:
        new_dict[items[0]] = items[1]

    return new_dict


convert_to_dict(tuple_list)

# what guy in video did

def convert_to_dict(tup_list):
    result_dict = {}
    for key, value in tup_list:
        result_dict.setdefault(key, value)
    return result_dict

# other way guy in video did

