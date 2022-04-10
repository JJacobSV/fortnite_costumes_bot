# List of costume names
costume_names = ['Eon', 'Skull Ranger', 'Double Helix', 'Galaxy', 'Royale Bomber', 'The Reaper',
                 'Merry Marauder', 'Ginger Gunner', 'Black Knight', 'Purple Glow Skull Trooper', 
                 'Renegade Raider', 'Aerial Assault Trooper', 'Recon Expert']

# List of costume prices
costume_prices = [10.69, 10.69, 10.69, 10.69, 10.69, 10.69, 15.50, 15.50, 15.50, 15.50, 19.99, 19.99, 19.99]

# List to store ordered costumes
order_list =[]
# List to store costume prices
order_cost =[]

# List to store order cost
def menu():
    number_costume = 13

    for count in range(number_costume):
        print("{} {} ${:.2f}"  .format(count+1,costume_names[count],costume_prices[count]))

menu()


def order_costume():
    # Ask for total number of pizza for order
    num_costumes = 0
    while True:  
        try:
            num_costumes = int(input("How many costumes do you want to order? "))
            if num_costumes >= 1 and num_costumes <= 15:
                break
            else:
                print("Your order must be between 1 and 15")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter a number between 1 and 15")
    # Choose costume from menu
    for item in range(num_costumes):
        while num_costumes > 0:
            while True:  
                try:
                    costume_ordered = int(input("Please choose the costume you would like to order by entering the number of the costume from the menu "))
                    if costume_ordered >= 1 and costume_ordered <= 13:
                        break
                    else:
                        print("Your costume order must be between 1 and 13")
                except ValueError:
                    print ("That is not a valid number")
                    print ("Please enter a number between 1 and 13")
            costume_ordered = costume_ordered -1
            order_list.append(costume_names[costume_ordered])
            order_cost.append(costume_prices[costume_ordered])
            print("{} ${:.2f}"  .format(costume_names[costume_ordered],costume_prices[costume_ordered]))
            num_costumes = num_costumes -1

menu()
order_costume()