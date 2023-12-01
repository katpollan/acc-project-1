allowed_username_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
username_input = input("Please enter a username: ") #gathers user's proposed handle
#sanitize user's input for username
sani_username_input = username_input.strip()

usernameinput_validation = set((sani_username_input))
if usernameinput_validation.issubset(allowed_username_characters) == False:
    print("Username can only contain letters, numbers, and underscores")
    print("Please try again.")

print(usernameinput_validation)

result = usernameinput_validation.issubset(allowed_username_characters)
print(result)