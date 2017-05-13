#Get the user's name
name = input("Enter your name: ")

#Reverse the name
i = len(name) - 1
print(i)
backwards_name = ""
while i >= 0:
    backwards_name += name[i]
    i -= 1
backwards_name = backwards_name.title()
print(backwards_name)

#If the name is a Palindrome print "Palindrome"
if(backwards_name == name):
    print("Palindrome!")
