# Bugs
# Will only work for valid input "d" and "p"
# Invalid input triggers else statement but program does not ask for input again.

# Menu so that user can choose either pickup or delivery

print ("Do you want to Click and Collect your order or would you like it to be Delivered")

print ("For Click and Collect enter p")
print ("For Delivery enter d")

pickup = input()

if pickup == "p":
    print ("Click and Collect")

elif pickup == "d":
    print ("Delivery")

else:
    print ("That was not a valid input")