# Bugs
# Will only work for valid input "d" and "p"
# Menu so that user can choose either pickup or delivery

print ("Do you want to Click and Collect or would you like it to be Delivered")

print ("For Click and Collect enter p, for Delivery enter d")

pickup = input()

if pickup == "p":
    print ("Click and Collect")

elif pickup == "d":
    print ("Delivery")