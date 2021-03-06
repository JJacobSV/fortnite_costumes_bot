# List to store ordered costumes
order_list =['Eon', 'Recon Expert', 'Aerial Assault Trooper', 'The Reaper']
# List to store costume prices
order_cost =[10.69, 19.99, 19.99, 10.69]

customer_details = {'name':'Jacob','phone':'0275198213','house':'110','street':'Aviemore Drive','suburb':'Highland Park'}

def print_order():
    total_cost = sum(order_cost)
    print("Customer Details")
    print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}"  .format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")

print_order()