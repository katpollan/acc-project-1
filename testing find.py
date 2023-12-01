special_characters = '!?@#^&*_-'
statement = 'helloo!'
statement2 = 'byeeeeeeeee'

# print(statement.find('!?@#^&*_-'))


# #so I think this is why i haven't been able to get this to work
# #those characters aren't searchable
# #awesome

# #testing if .__contains__ works
# print(statement.__contains__(special_characters))
# print(statement.__contains__('!?@#^&*_-'))
# #nope

#directly copied from geeks for geeks to play with the code and see how it works

'''
n = "Geeks$For$Geeks"
n.split()
c = 0
s = '[@_!#$%^&*()<>?/\|}{~:]'  # special character set
for i in range(len(n)):
    # checking if any special character is present in given string or not
    if n[i] in s:
        c += 1   # if special character found then add 1 to the c
 
# if c value is greater than 0 then print no
# means special character is found in string
if c:
    print("string is not accepted")
else:
    print("string accepted")

#i wanted to see what this was
print(n.split())
'''

statement.split()
c=0
for s in range(len(statement)):
    if statement[s] in special_characters:
        c +=1
if c:
    print('no')
else:
    print('yep')

print(c)

statement2.split()
c=0
for s in range(len(statement2)):
    if statement2[s] in special_characters:
        c +=1
if c:
    print('no')
else:
    print('yep')

print(c)
#yay I think that works


#testing it for userinput now

userinput = input("type something here ho:")
#userinput.split()
counter=0

for s in range(len(userinput)):
    if userinput[s] in special_characters:
        counter +=1
if counter == 0:
    print('no ho')
else:
    print('yay')
print(counter)
#yay this works, now to put in the OTHER code
#no it didn't my brain is dumb
