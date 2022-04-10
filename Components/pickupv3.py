# Customer details dictionary
customer_details = {}

# Basic instructions
print("Please enter your Name and Phone number")

# Customer name not blank
valid = False
while not valid:
    customer_details['name'] = input("Insert Name, ")
    if customer_details['name'] != "":
        print (customer_details['name'])
        break
    else:
        print("Sorry this cannot be left blank")

# Customer phone number not blank
valid = False
while not valid:
    customer_details['phone'] = input("Insert Phone number, ")
    if customer_details['phone'] != "":
        print (customer_details['phone'])
        break
    else:
        print("Sorry this cannot be left blank")