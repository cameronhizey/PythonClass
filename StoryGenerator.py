def sentence_maker(text):
    question_words = ["what", "how", "when"]
    capitalize_text = text.capitalize()
    for word in question_words:
        if text.startswith(word):
            return "{}?".format(capitalize_text)
    return "{}.".format(capitalize_text)


result = []
while True:
    user_input = input("What is on your mind?")
    if user_input == '\\end':
        break
    else:
        complete_sentence = sentence_maker(user_input)
        result.append(complete_sentence)
story = " ".join(result)
print(story)