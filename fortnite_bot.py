# Fornite Costume Bot
# 10/04/22
# Bugs - Phone number input allows letters
#      - Name input allows numbers

# Known Bugs
# 11/04/22 - Final printout is not printing customer details correctly - Fixed

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


def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be left blank")

def check_string(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("Input must only contain letters")
        else:
            return response.title()


# Validates inputs to check if they are an integer
def val_int(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print (f"Please enter a number between {low} and {high}")
        except ValueError:
            print ("That is not a valid number")
            print (f"Please enter a number between {low} and {high}")


def check_phone(question, PH_LOW, PH_HIGH):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= PH_LOW and count <= PH_HIGH:
                return str(num)
            else:
                print("NZ Phone numbers have between 7 and 10 digits")
        except ValueError:
            print("Please enter a number ")

# Welcome message with random name
def welcome():
    num = randint(0, 9)
    name = (names[num])
    print("********************************************")
    print("********* Fortnite Battlpass Skins *********")
    print("********************************************")
    print("")
    print("*** Welcome to Fortnite Battlepass skins ***")
    print("*** My name is", name, "***")
    print("*** I will be here to help you order "
          "your FAVORITE Fortnite costumes ***")


# Menu for pickup or delivery
def ordertype():
    print ("")
    del_pick = ""
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Is your order for Click and Collect "
           "or would you like it to be Delivered")
    print ("For Click and Collect enter 1")
    print ("For Delivery enter 2 (A $9 fee will be applied for less than 5 costumes ordered)")
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print ("Click and Collect")
        del_pick = "Click and Collect"
        pickup_info()
    else:
        print ("Delivery")
        delivery_info()
        del_pick = "Delivery"
    return del_pick


# Pick up information - name and phone number
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    print (customer_details['phone'])


# Delivery function - name, address and phone
# free for 5 or more costumes otherwise $9 fee
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    print (customer_details['phone'])

    question = ("Please enter your House number ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = check_string(question)
    print (customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = check_string(question)
    print (customer_details['suburb'])


# Costume Menu
def menu():
    print ("")
    number_costumes = 13
    for count in range(number_costumes):
        print("{} {} ${:.2f}"  .format(count+1, costume_names[count],
              costume_prices[count]))

# Costume order - from menu - Print each costume ordered with cost
# Choose total number of costumes - Max 15


def order_costume():
    # Ask for total number of costumes for order
    num_costumes = 0
    NUM_LOW = 1
    NUM_HIGH = 15
    MENU_LOW = 1
    MENU_HIGH = 13
    question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ")
    print("")
    print("How many costumes do you want to order? ")
    num_costumes = val_int(NUM_LOW, NUM_HIGH, question)
    # Choose costume from menu
    for item in range(num_costumes):
        while num_costumes > 0:
            print("Please choose the costume you would like to"
                  " order by entering the number of the costume from the menu ")
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ")
            print("")
            costume_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            costume_ordered = costume_ordered - 1
            order_list.append(costume_names[costume_ordered])
            order_cost.append(costume_prices[costume_ordered])
            print("{} ${:.2f}" .format(costume_names[costume_ordered],
                  costume_prices[costume_ordered]))
            num_costumes = num_costumes - 1


# Print order out - including if order is del or pick up and names
# and price of each pizza - total cost including any delivery charge
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print("Customer Details")
    if del_pick == "Click and Collect":
        print("Your Order is for Click and Collect")
        print(f"Customer Name: {customer_details['name']}"
              f"\nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "Delivery":
        print("Your Order is for Delivery")
        print(f"Customer Name: {customer_details['name']}"
              f"\nCustomer Phone: {customer_details['phone']}"
              f"\nCustomer Address: {customer_details['house']} "
              f"{customer_details['street']} {customer_details['suburb']}")
    print()
    # Turn into function later so that code is not repeated so much
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}"  .format(item, order_cost[count]))
        count = count+1
    print()
    if del_pick == "Delivery":
        if len(order_list) >= 5:
            print("Your order will be delivered for free")
        elif len(order_list) <= 5:
            print("There is an additional $9.00 delivery charge")
            total_cost = total_cost + 9
    print("Total Order Cost")
    print(f"${total_cost:.2f}")
    if del_pick == "Click and Collect":
        print ("Thank you for your order, we'll let you know when its ready")
    elif del_pick == "Delivery":
        print("Thank you for your order, it will be delivered soon")
        print("")


# Ability to cancel or proceed with order
def confirm_cancel():
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Please confirm your order")
    print ("To confirm please enter 1")
    print ("To cancel please enter 2")
    print ("")
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print ("Your Order Has Been Confirmed")
        print ("Your order has been sent to our warehouse")
        print ("Your order will be with you shortly")
        new_exit()
    elif confirm == 2:
        print ("Your Order Has Been Cancelled")
        print ("You can restart your order or exit the BOT")
        new_exit()


# Option for new order or to exit
def new_exit():
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("")
    print ("Do you want to start another Order or Exit?")
    print ("To start another order enter 1")
    print ("To exit the BOT enter 2")
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print ("New Order")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()

    elif confirm == 2:
        print ("Exit")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit()


# Main Function
def main():
    welcome()
    del_pick = ordertype()
    menu()
    order_costume()
    print_order(del_pick)
    confirm_cancel()

main()
