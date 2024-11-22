from pprint import pprint
programming_language = [
    {"user_name" : "Elshad",
     "favorite_languages" : ["Python", "Java", "C#"],
     "experience": 10
    },
    {"user_name":"Renad",
     "favorite_languages" : ["Scratch","Python"],
     "experience" : 2
    },
]
# what i did
# def add_new_user(p_user, p_favorite, p_years):
#     programming_language.append({"user_name" : p_user,
#                                  "favorite_languages" : p_favorite,
#                                  "experience" : p_years},)
#     return programming_language

# add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10)
# print(programming_language)

# What guy in video did
def add_new_user(p_username, p_favorite_language, p_experience):
    new_user = {}
    new_user["user_name"] = p_username
    new_user["favorite_languages"] = p_favorite_language
    new_user["experience"] = p_experience
    programming_language.append(new_user)

add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10)

pprint(programming_language)