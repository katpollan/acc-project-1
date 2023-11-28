#list for usernames
verified_usernames = ["admin","admin123","root"]
#list for passwords
verified_passwords = ["Adminpass1!,tesTpass3","pasSs123"]

#set for allowed username characters
allowed_username_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
#set to test if password has allowed characters
special_password_characters = set("!?@#^&*_-")

#program opening
print("Hello!")
print("Please create a username and password.")
print("Username must:")
print("Start with a lower case letter/n Only contain letters, numbers and underscores")
print("Not be already in use")
print("Password must:")
print("Be at least 8 letters long /n Contains at least 1 uppercase letter/n Contains 1 lowercase letter")
print("Contains at least one digit/n Contains at least one of these characters:!,?,@,#,^,&,*,_,- ")
print("Doesn't contain any spaces")

#user input for username
username_input = input("Please enter a username: ") #gathers user's proposed handle
#sanitize user's input for username
sani_username_input = username_input.strip()

#start Username verfifaction
#checking if username starts with lowercase
username_lowercase = sani_username_input.lower(0)
while username_lowercase == False:
    print("Username must start with a lowercase letter.")
    print("Please try again.")
    
   #else:
    #continue

#checking if username has letters, numbers and underscores
usernameinput_validation = set((sani_username_input))
if usernameinput_validation.issubset(allowed_username_characters) == False:
  print("Username can only contain letters, numbers, and underscores")
  print("Please try again.")
  
  #else:
   #continue

#checking if username is taken
if sani_username_input in verified_usernames == True:
  print("That username is taken.")
  print("Please try again.")
# else:
   #continue

#gathering user input for password
userpassword_input = input("Please enter a password:" )

#sanitize user's input for password
sani_userpass_input = userpassword_input.strip()

#start Password verifaction
#checking password length
password_length = len(sani_userpass_input)
if sani_userpass_input == password_length <8:
  print("Password must be at least 8 characters.")
  print("Please try again.")
# else:
#    #continue

#checking if password has an uppercase letter
password_uppercase = sani_userpass_input.isupper()
if password_uppercase == False:
  print("Password must contain at least one uppercase letter")
  print("Please try again")
else:
   #continue

#checking if password has a lowercase letter
password_lowercase = sani_userpass_input.islower()
if password_lowercase == False:
  print("Password must contain at least one lowercase letter")
  print("Please try again")
else:
   #continue

#checking to see if password has a number
password_number = sani_userpass_input.isdigit()
if password_number == False:
  print("Password must contain at least one number")
  print("Please try again")

password_specialcharacters = set((sani_userpass_input))
if usernameinput_validation.issubset(special_password_characters) == False:
  print ("Password must contain one of these characters: !?@#^&*_-")
  print("Please try again.")
else:
   #continue

#User has completed verifaction


#add username and passwords to list
verified_usernames.append(sani_username_input)
verified_passwords.append(sani_userpass_input)

print("Thank you! Sign up successful.")
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

#create zip+dictonary to verify that username+pass go together