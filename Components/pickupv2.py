# Bug - accepts blank input

print("Please enter your Name and Phone number")

# Customer name
valid = False
while not valid:
    name = input("Insert Name, ")
    if name != "":
        print (name)
        break
    
    else:
        print("Sorry this cannot be left blank")

# Customer phone number
valid = False
while not valid:
    phone = input("Insert Phone number, ")
    if phone != "":
        print (phone)
        break
    
    else:
        print("Sorry this cannot be left blank")
