#program opening
print("Hello!")
print("Please create a username and password.")
print("Username must be between 5 and 13 characters, cannot be taken, and contain only letters.")
print("Password must be between 8 and 16 characters and contain at least one uppercase letter.")

#list for usernames
verified_usernames = ["admin","testuser","useruser"]
#list for passwords
verified_passwords = ["Adminpass1!,tesTpass3","pasSs123"]

#user input for username
username_input = input("Please enter a username: ")
#sanitize user's input for username
sani_username_input = username_input.strip()

#start Username verfifaction
#checking username length
username_length = len(sani_username_input)
if sani_username_input == username_length <5 or username_length >13:
    print("Username must be between 5 and 13 characters.")
    print("Please try again.")
else:
   continue

#checking if username only has letters
username_alpha = sani_username_input.isalpha()
if username_alpha == False:
  print("Username can only contain letters")
  print("Please try again.")
else:
   continue

#checking if username is taken
if sani_username_input in verified_usernames == True:
  print("That username is taken.")
  print("Please try again.")
else:
   continue

#gathering user input for password
userpassword_input = input("Please enter a password:" )

#sanitize user's input for password
sani_userpass_input = userpassword_input.strip()

#start Password verifaction
#checking password length
password_length = len(sani_userpass_input)
if sani_userpass_input == password_length <8 or password_length >16:
  print("Password must be between 8 and 16 characters.")
  print("Please try again.")
else:
   continue

#checking if password has an uppercase letter
password_uppercase = sani_userpass_input.isupper()
if password_uppercase == False:
  print("Password must contain at least one uppercase letter")
  print("Please try again")
else:
   continue

#checking if password has a lowercase letter
password_lowercase = sani_userpass_input.islower()
if password_lowercase == False:
  print("Password must contain at least one lowercase letter")
  print("Please try again")
else:
   continue
#User has completed verifaction

#add username and passwords to list
verified_usernames.append(sani_username_input)
verified_passwords.append(sani_userpass_input)

print("Thank you! Your user name and password are verified.")
print("Please log in.")

#gathering users login input
user_name = input('Please enter your username' ) #gathers user's handle
user_password = input ('Please enter your password' ) #gathers user's password

#sanitizing the user inputs
sani_inputusername = user_name.strip() #sanitizes the user name
sani_inputpassword = user_password.strip() #sanitizes the password

if sani_inputusername in verified_usernames == True and sani_inputpassword in verified_passwords == True:
    print('Login Successful')

else:
  print("Incorrect user name or password")
  print("Please try again.")