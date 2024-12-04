def most_frequent(p_tuple):
    max_num = 0
    letter = p_tuple[0]
    for items in p_tuple:
        value = p_tuple.count(items)
        if value > max_num:
            max_num = value
            letter = items
    return letter, max_num




my_tuple = ("a", "b", "c", "d", "e", "a", "c", "e", "b", "e", "c", "a", "f", "e", "r")
print(most_frequent(my_tuple))

# guy in videos version

def most_frequent(p_tuple):
    v_count = 0
    item = p_tuple[0]
    for value in p_tuple:
        current_item_count = p_tuple.count(value)
        if current_item_count > v_count:
            v_count = current_item_count
            item = value
    return (item, v_count)
    # return {"item" : item, "frequency" : v_count}

print(most_frequent(my_tuple))
