# Fornite Costume Bot
import random
from random import randint

#List of random names
names = ["Banana", "Alvin", "Hannah", "Marquis", "Emily","Christy", "Carlos", "Theodore", "Simon", "Shaniqa"]

# Customer details dictionary
customer_details = {}

# Validates inputs to check of theu are blank
def not_blank(question):
    valid = False    
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be left blank")

# Welcome message with random name
def welcome():
    num = randint(0,9) 
    name = (names[num])
    print("*** Welcome to Fortnite Battlepass skins ***")
    print("*** My name is",name, "***")
    print("*** I wil be here to help you order your FAVORITE Fortnite costumes ***")


# Menu for pickup or delivery
def ordertype():
    print ("Is your order for Click and Collect or would you like it to be Delivered")
    print ("For Click and Collect enter 1")
    print ("For Delivery enter 2")

    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Click and Collect")
                    pickup()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    break
            else:
                print ("The number must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")


# Pick up information - name and phone number
def pickup():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    #print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    #print (customer_details['phone'])
    print(customer_details)



# Delivery function - name, address and phone, free for 5 or more costumes otherwise $9 fee




# Choose total number of costumes 



# Costume Menu



# Costume order - from menu - Print each costume ordered with cost




# Print order out - including if order is del or pick up and names and price of each pizza - total cost including any delivery charge 


# Ability to cancel or proceed with order



# Option for new order or to exit


# Main Function
def main():
    welcome()
    ordertype()

main()