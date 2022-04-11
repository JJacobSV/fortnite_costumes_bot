import sys


# List to store ordered costumes
order_list =[]
# List to store costume prices
order_cost =[]

# Customer details dictionary
customer_details = {}


print ("Do you want to start another Order or Exit?")
print ("To start another order enter 1")
print ("To exit the BOT enter 2")
while True:
    try:
        confirm = int(input("Please enter a number "))
        if confirm >= 1 and confirm <= 2:
            if confirm == 1:
                print ("New Order")
                order_list.clear()
                order_cost.clear()
                customer_details.clear()
                main()
                break

            elif confirm == 2:
                print ("Exit")
                order_list.clear()
                order_cost.clear()
                customer_details.clear()
                sys.exit()
                break
        else:
            print ("The number must be 1 or 2")
    except ValueError:
        print ("That is not a valid number")
        print ("Please enter 1 or 2")

def main():
    print("Start again")