def first_last_characters(word):
    if len(word) < 2:
        return ""
    else:
        new_word1 = word[:2]
        new_word2 = word[-2:]
        return new_word1 + new_word2


print(first_last_characters('appmillers'))
