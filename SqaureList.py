# sqaures numbers in a list
custom_list = [1, 2, 3, 4, 5]


def square_list(p_list):
    for index in range(len(p_list)):
        p_list[index] = (index + 1) * (index + 1)
    return p_list


print(square_list(custom_list))
