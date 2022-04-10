# List of costume names
costume_names = ['Eon', 'Skull Ranger', 'Double Helix', 'Galaxy', 'Royale Bomber', 'The Reaper',
                 'Merry Marauder', 'Ginger Gunner', 'Black Knight', 'Purple Glow Skull Trooper', 
                 'Renegade Raider', 'Aerial Assault Trooper', 'Recon Expert']

# List of costume prices
costume_prices = [10.69, 10.69, 10.69, 10.69, 10.69, 10.69, 15.50, 15.50, 15.50, 15.50, 19.99, 19.99, 19.99]

# List to store ordered costumes
order_list = []
# List to store costume prices
order_cost = []


def menu():
    number_costumes = 13

    for count in range (number_costumes):
        print("{} {} ${:.2f}"  .format(count+1,costume_names[count],costume_prices[count]))

menu()


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

print(num_costumes)

# Choose costume from menu
print ("Please choose the costume you would like to order by entering the number of the costume from the menu ")
for item in range(num_costumes):
    while num_costumes > 0:
        costume_ordered = int(input())
        order_list.append(costume_names[costume_ordered])
        order_cost.append(costume_prices[costume_ordered])
        num_costumes = num_costumes-1

print(order_list)
print(order_cost)