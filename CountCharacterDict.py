def count_character(p_word):
    my_dict = {}
    p_len = len(p_word)
    for key in p_word:
        counter = p_word.count(key, 0, p_len)
        if key not in my_dict:
            my_dict[key] = counter
    return my_dict



print(count_character("babacdas"))

# What guy in video did
# def count_character(word):
#     output_dict = dict()
#     for character in word:
#         if character not in output_dict:
#             output_dict[character] = 1
#         else:
#             output_dict[character] = output_dict[character] + 1
#     return output_dict
#
# print(count_character("babadacs"))