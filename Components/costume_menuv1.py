costume_names = ['Eon', 'Skull Ranger', 'Double Helix', 'Galaxy', 'Royale Bomber', 'The Reaper',
                 'Merry Marauder', 'Ginger Gunner', 'Black Knight', 'Purple Glow Skull Trooper', 
                 'Renegade Raider', 'Aerial Assault Trooper', 'Recon Expert']

costume_prices = [10.69, 10.69, 10.69, 10.69, 10.69, 10.69, 15.50, 15.50, 15.50, 15.50, 19.99, 19.99, 19.99]

number_costumes = 13

#print("How many costumes would you like to order?")
#num_costume = int(input())

for count in range (number_costumes):
    print (count,costume_names[count],costume_prices[count])