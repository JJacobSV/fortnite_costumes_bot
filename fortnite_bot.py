# Fornite Costume Bot
# 10/04/22
# Bugs - Phone number input allows letters - Fixed
#      - Name input allows numbers - Fixed

# Known Bugs
# 11/04/22 - Final printout is not printing customer details correctly - Fixed
# imports random
import sys
import random
from random import randint

# Constants
LOW = 1
HIGH = 2
PH_LOW = 7
PH_HIGH = 10

# List of random names
names = ["Banana", "Alvin", "Hannah", "Marquis", "Emily",
         "Christy", "Carlos", "Theodore", "Simon", "Shaniqa"]

# List of costume names
costume_names = ['Eon', 'Skull Ranger', 'Double Helix', 'Galaxy',
                 'Royale Bomber', 'The Reaper',
                 'Merry Marauder', 'Ginger Gunner', 'Black Knight',
                 'Purple Glow Skull Trooper',
                 'Renegade Raider', 'Aerial Assault Trooper', 'Recon Expert']

# List of costume prices
costume_prices = [10.69, 10.69, 10.69, 10.69, 10.69, 10.69,
                  15.50, 15.50, 15.50, 15.50, 19.99, 19.99, 19.99]

# List to store ordered costumes
order_list = []
# List to store costume prices
order_cost = []

# Customer details dictionary
customer_details = {}

# Validates inputs to check if they are blank


def not_blank(question): # define following program as not_blank
    valid = False # valid = false
    while not valid: # When valid is not false
        response = input(question) # Asks the user the question
        if response != "": # if response is inputted correctly then contine with program
            return response.title()
        else: # if input is blank prints error message
            print("This cannot be left blank") # Error message


def check_string(question): # function for letters only
    while True: # Creates loop
        response = input(question) # displays question
        x = response.isalpha()
        if x == False: # if input was not in letters print error message
            print("Input must only contain letters") # Error message
        else: # Else it continues with code
            return response.title() 

# Validates inputs to check if they are an integer
def val_int(low, high, question): # creates function for question that need a low or high input
    while True: # Creates loop
        try: 
            num = int(input(question)) # input give to question = number
            if num >= low and num <= high: # if number is less than low number or higher than high number
                return num # continues code as number inputted is valid 
            else: # Else prints error message for numbers lower or higher than 1 and 2 
                print (f"Please enter a number between {low} and {high}")
        except ValueError: # If the input was not an integer prints it is not a valid number and prints error message
            print ("That is not a valid number") # Prints invalid number
            print (f"Please enter a number between {low} and {high}") # prints error message


def check_phone(question, PH_LOW, PH_HIGH): # function for phone number being integers only
    while True: # Creates loop
        try:
            num = int(input(question)) # asks question
            test_num = num 
            count = 0 # sets count to 0
            while test_num > 0: # when test_num is is greater than 0
                test_num = test_num//10 # if num is greater than 0 divide by 10
                count = count + 1 # count is equal to count + 1 
            if count >= PH_LOW and count <= PH_HIGH: # if count is between low and high
                return str(num) # returns input
            else: # else prints error message
                print("NZ Phone numbers have between 7 and 10 digits") # prints error message
        except ValueError: # if users input is a letter tells them to input a number
            print("Please enter a number ") # prints error message 


# Welcome message with random name
def welcome(): # function for welcoming the user
    num = randint(0, 9) # chooses a random number from the random names
    name = (names[num]) # name is equal to the name that was chosen from the random number chosen for the random names list
    print("********************************************") # prints asterisk for sign
    print("********* Fortnite Battlpass Skins *********") # prints asterisk with shop name
    print("********************************************") # prints asterisk for sign
    print("") # prints blank
    print("*** Welcome to Fortnite Battlepass skins ***") # prints welcome to shop message
    print("*** My name is", name, "***") # prints welcome message
    print("*** I will be here to help you order "
          "your FAVORITE Fortnite costumes ***") # notifys user that theu will be there to assist the user oredering


# Menu for pickup or delivery
def ordertype(): # function for the ordering type
    print ("") # prints blank space
    del_pick = "" # del_pick is equal to input
    question = (f"Enter a number between {LOW} and {HIGH} ") # creates question to enter a number between low or high constants
    print ("Is your order for Click and Collect " 
           "or would you like it to be Delivered "
           "(A $9 fee will be applied for less than 5 costumes ordered)") # asks user if their order is for click and collect or delivery
    print ("For Click and Collect enter 1") # prints message for click and collect
    print ("For Delivery enter 2") # prints message for delivery
    delivery = val_int(LOW, HIGH, question) # makes sure integer given is between LOW and HIGH constants
    if delivery == 1: # if delivery is equally equal to 1
        print ("Click and Collect") # print click and collect
        del_pick = "Click and Collect" # del_pick is set to click and collect
        pickup_info() # uses pickup_info function
    else: # if pickup doesn't equally equal to 1
        print ("Delivery") # prints delivery
        delivery_info() # uses delivery_info function
        del_pick = "Delivery" # del_pick is set to click and collect
    return del_pick # returns input


# Pick up information - name and phone number
def pickup_info(): # function for pickup information 
    question = ("Please enter your name ") # sets question
    customer_details['name'] = check_string(question) # asks user question, saves name to customer details
    print (customer_details['name']) # prints the customer_details for name

    question = ("Please enter your phone number ") # sets question
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH) # asks user question, saves phone number to customer details
    print (customer_details['phone']) # prints the customer_details for name


# Delivery function - name, address and phone
# free for 5 or more costumes otherwise $9 fee
def delivery_info(): # function for delivery info
    question = ("Please enter your name ") # sets question
    customer_details['name'] = check_string(question) # asks user question, saves name to customer details
    print (customer_details['name']) # prints the customer_details for name

    question = ("Please enter your phone number ") # sets question
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH) # asks user question, saves phone number to customer details
    print (customer_details['phone']) # prints the customer_details for phone number

    question = ("Please enter your House number ") # sets question
    customer_details['house'] = not_blank(question) # asks user question, saves house number to customer details
    print (customer_details['house']) # prints the customer_details for house number

    question = ("Please enter your street name ") # sets question
    customer_details['street'] = check_string(question) # asks user question, saves street to customer details
    print (customer_details['street']) # prints the customer_details for street

    question = ("Please enter your suburb ") # sets question
    customer_details['suburb'] = check_string(question) # asks user question, saves suburb to customer details
    print (customer_details['suburb']) # prints the customer_details for suburb


# Costume Menu
def menu(): # function for menu
    print("") # prints blank space
    number_costumes = 13 # number of costumes I am selling
    for count in range(number_costumes): # when count is in range of the number or costumes
        print("{} {} ${:.2f}"  .format(count+1, costume_names[count], # formats the way costumes are displayed
              costume_prices[count]))

# Costume order - from menu - Print each costume ordered with cost
# Choose total number of costumes - Max 15


def order_costume(): # function for ordering costumes
    # Ask for total number of costumes for order
    num_costumes = 0 # sets the count to 0
    NUM_LOW = 1 # sets NUM_LOW constant to 1
    NUM_HIGH = 15 # sets NUM_HIGH constant to 15
    MENU_LOW = 1 # sets MENU_LOW constant to 1
    MENU_HIGH = 13 # sets MENU_HIGH constant to 13
    question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ") # sets question
    print("") # prints blank space
    print("How many costumes do you want to order? ") # prints question for how many costumes does the user want to order
    num_costumes = val_int(NUM_LOW, NUM_HIGH, question) # when user inputs, check input to see whether it is between NUM_LOW and NUM_HIGH constant
    # Choose costume from menu
    for item in range(num_costumes): 
        while num_costumes > 0: # while num_costumes is greater than 0
            print("Please choose the costume you would like to " # prints question
                  "order by entering the number of the costume from the menu ")
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ") # sets question
            print("") # prints blank space
            costume_ordered = val_int(MENU_LOW, MENU_HIGH, question) # makes sure integer inputted is between MENU_LOW and MENU_HIGH
            costume_ordered = costume_ordered - 1 # makes sure correct costume is ordered by minusing 1 to equal the right costume
            order_list.append(costume_names[costume_ordered]) # links users integer to chosen costume
            order_cost.append(costume_prices[costume_ordered]) # links users integer to chosen 
            print("{} ${:.2f}" .format(costume_names[costume_ordered], # formats the ordered costumes
                  costume_prices[costume_ordered]))
            num_costumes = num_costumes - 1 # creates loop by minusing 1 till it reaches 0 breaking the loop


# Print order out - including if order is del or pick up and names
# and price of each pizza - total cost including any delivery charge
def print_order(del_pick): # function for printing out the order details
    print("") # print blank space
    total_cost = sum(order_cost) # total cost equals the sum of the order cost
    print("Customer Details") # prints message saying customer details
    if del_pick == "Click and Collect": # if delivery type is click and collect
        print("Your Order is for Click and Collect") # prints that their order is for click and collect
        print(f"Customer Name: {customer_details['name']}" # prints the customers name from customer details
              f"\nCustomer Phone: {customer_details['phone']}") # prints the customers phone number from customer details
    elif del_pick == "Delivery": # else if it is delivery 
        print("Your Order is for Delivery") # prints their order is for delivery
        print(f"Customer Name: {customer_details['name']}" # prints the customers name from customer details
              f"\nCustomer Phone: {customer_details['phone']}" # prints the customers phone number from customer details
              f"\nCustomer Address: {customer_details['house']} " # prints the customers house number from customer details
              f"{customer_details['street']} {customer_details['suburb']}") # prints the customers street name and suburb from customer details
    print() # prints blank space
    # becomes a function
    print("Order Details") # prints order details
    count = 0 # sets count to 0
    for item in order_list: # for the items in the order_list
        print("Ordered: {} Cost ${:.2f}"  .format(item, order_cost[count])) # prints formated order details
        count = count+1 # count which is 0 is equal to count +1 
    print() # prints blank space 
    if del_pick == "Delivery": # if delivery is picked
        if len(order_list) >= 5: # if costumes ordered are greater than 5
            print("Your order will be delivered for free") # prints that their will be no delivery no fee
        elif len(order_list) <= 5: # else if costumes ordered are less than 5
            print("There is an additional $9.00 delivery charge") # prints that there is a additional $9 delivery charge
            total_cost = total_cost + 9 # total cost of the costumes ordered adds 9 for delivery fee
    print("Total Order Cost") # prints total order cost
    print(f"${total_cost:.2f}") # prints total order cost including any delivery fee
    if del_pick == "Click and Collect": # if it is click and collect 
        print ("Thank you for your order, we'll let you know when its ready") # prints that their order will be ready
    elif del_pick == "Delivery": # if it is delivery
        print("Thank you for your order, it will be delivered soon") # print thank you for your order it will be delivered soon
        print("") # prints blank space


# Ability to cancel or proceed with order
def confirm_cancel(): # function to confirm or cancel order
    question = (f"Enter a number between {LOW} and {HIGH} ") # sets question
    print ("Please confirm your order") # prints message to confirm their order
    print ("To confirm please enter 1") # prints that to confirm press 1
    print ("To cancel please enter 2") # prints that to cancel press 2
    print ("") # prints blank space
    confirm = val_int(LOW, HIGH, question) # makes sure integer is between LOW and HIGH constant
    if confirm == 1: # to confirm order it must equal 1
        print ("Your Order Has Been Confirmed") # prints their order is confirmed
        print ("Your order has been sent to our warehouse") # prints that their order has been sent to our warehouse
        print ("Your order will be with you shortly") # prints their order will be with them shortly
        new_exit() # uses new_exit function
    elif confirm == 2: # else if confirm is set to 2 
        print ("Your Order Has Been Cancelled") # prints their order is cancelled
        print ("You can restart your order or exit the BOT") # prints that they can restart an order or exit the bot
        new_exit() # uses new_exit function


# Option for new order or to exit
def new_exit(): # function for new order or exit
    question = (f"Enter a number between {LOW} and {HIGH} ") # sets question
    print ("") # prints blank space
    print ("Do you want to start another Order or Exit?") # prints whether they want to start another order or exit
    print ("To start another order enter 1") # prints that to start another order enter 1
    print ("To exit the BOT enter 2") # prints that to exit the bot enter 2
    confirm = val_int(LOW, HIGH, question) # checks if integer inputted is between LOW and HIGH constants
    if confirm == 1: # if confirm is equal to 1
        print ("New Order") # prints new order
        order_list.clear() # clears the order list
        order_cost.clear() # clears the cost list
        customer_details.clear() # clears the customers details
        main() # restarts code

    elif confirm == 2: # else if confirm is equal to 2 
        print ("Exit") # prints exit
        order_list.clear() # clears order list
        order_cost.clear() # clears cost list
        customer_details.clear() # clears the customers details
        sys.exit() # closes the program


# Main Function
def main(): 
    welcome() # runs welcome function
    del_pick = ordertype() # runs order type function
    menu() # runs menu function
    order_costume() # runs order costume function
    print_order(del_pick) # runs print order function
    confirm_cancel() # runs confirm or cancel function

main() # runs the whole code
