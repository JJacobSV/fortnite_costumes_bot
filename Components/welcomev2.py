import random
from random import randint

#List of random names
names = ["Banana", "Alvin", "Hannah", "Marquis", "Emily","Christy", "Carlos", "Theodore", "Simon", "Shaniqa"]

def welcome():
    num = randint(0,9) 
    name = (names[num])
    print("*** Welcome to Fortnite Battlepass skins ***")
    print("*** My name is",name, "***")
    print("*** I wil be here to help you order your FAVORITE Fortnite costumes ***")

def main():
    welcome()

main()