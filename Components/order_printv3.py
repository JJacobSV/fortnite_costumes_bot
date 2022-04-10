# List to store ordered costumes
order_list =['Eon', 'Recon Expert', 'Aerial Assault Trooper', 'The Reaper']
# List to store costume prices
order_cost =[10.69, 19.99, 19.99, 10.69]

customer_details = {'name':'Jacob','phone':'0275198213','house':'110','street':'Aviemore Drive','suburb':'Highland Park'}

print(f"{customer_details['name']} {customer_details['phone']} {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}"  .format(item, order_cost[count]))
    count = count+1