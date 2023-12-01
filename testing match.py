verified_usernames = ["admin","admin123","root"]
username_input = input('type a username here:')
sani_username_input = username_input.strip()

for u in verified_usernames:
      if (u == sani_username_input):
            print('this is taken')

print(u)
print(verified_usernames)