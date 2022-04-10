# Menu so that user can choose either pickup or delivery

# Bug - need to make it so that it only accepts 1 or 2

print ("Is your order for Click and Collect or would you like it to be Delivered")

print ("For Click and Collect enter 1")
print ("For Delivery enter 2")

low =1
high = 2

while True:
    try:
        pickup = int(input("Please enter a number "))

        if pickup == 1:
            print ("Click and Collect")
            break

        elif pickup == 2:
            print ("Delivery")
            break

    except ValueError:
        print ("That is not a valid number")
        print ("Please enter 1 or 2")