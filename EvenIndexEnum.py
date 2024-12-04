my_tuple = ("a", "b", "c", "d", "e", "f", "g")


def even_index_items(p_tuple):
    new_list = []
    for index, value in enumerate(p_tuple):
        if index % 2 == 0:
            new_list += value
    new_tuple = tuple(new_list)
    return new_tuple


result_tuple = even_index_items(my_tuple)
print(result_tuple)
