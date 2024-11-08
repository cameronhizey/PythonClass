#
def password_controller(password):
    if len(password) > 8:
        return "Success"
    else:
        return "The password has to be more than 8 characters"


custom_password = input("What is your password?")
result = password_controller(custom_password)
print(result)
