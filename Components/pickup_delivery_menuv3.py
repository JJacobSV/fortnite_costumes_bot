# Menu so that user can choose either pickup or delivery

print ("Is your order for Click and Collect or would you like it to be Delivered")

print ("For Click and Collect enter 1")
print ("For Delivery enter 2")

pickup = int(input())

if pickup == 1:
    print ("Click and Collect")

elif pickup == 2:
    print ("Delivery")

else:
    print ("That was not a valid input")