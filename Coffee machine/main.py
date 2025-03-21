import art
import sys
from os import system, name
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')
machine="off"
resources = {
    "Water" : [500,'ml'],
    "Milk" : [1000,'ml'],
    "Coffee" : [100,'g'],
}
recipe = {
    "Espresso":[70,0,18],
    "Latte": [200,150,24],
    "Cappuccino": [250, 100, 24],
}
menu = {
        "Espresso": 70,
        "Latte": 50,
        "Cappuccino": 60,
    }
def display_menu():
    print("MENU:\n")
    for order in menu:
        print(f"{order} = Rs.{menu[order]}")
#Function to display the logo, report instruction detail, to ask the user for their choice of coffee
def display():

    print("Enter 'report' to get the ingredient details.")
    display_menu()
    type = input("What would you like?: \n")
    return type
#function to display the report of resources
def display_report():
    global resources
    for item in resources:
        print(f"{item} = {resources[item]}")
def sufficiency_check(type):
    global resources
    req_water = recipe[type][0]
    req_milk = recipe[type][1]
    req_coffee = recipe[type][2]

    if req_water>resources["Water"][0] and req_milk>resources["Milk"][0] and req_coffee>resources["coffee"][0]:
        return "Sorry, Not Sufficient ingredients."
    else:
        return type
#Function to ask user to make the payment.
def make_payment(order):
    global menu
    bill = menu[order]
    print(f"Your bill is of {bill}")
    tens = int(input("How many Tens: "))
    twenties = int(input("How many Twenties: "))
    fifties = int(input("How many Fifties: "))
    hundreds = int(input("How many Hundreds: "))
    total = (10*tens)+(20*twenties)+(50*fifties)+(100*hundreds)
    if total>bill:
        refund = total-bill
        print(f"Here is your change. {refund}\nYour coffee will start preparing now.")
    elif total==bill:
        print(f"Your coffee will start preparing now.")
    else:
        print(f"Amount you paid is not sufficient.")
        sys.exit()

#Function to make the coffee and give the final outcome to the user.
def make_coffee(order):
    print("Here is your coffee")
    print(art.coffee)
    modify_resources(order)

def modify_resources(order):
    global resources
    resources["Water"][0] -= recipe[order][0]
    resources["Milk"][0] -= recipe[order][1]
    resources["Coffee"][0] -= recipe[order][2]
def power():
    print("Turn off the machine if there are no users.")
    machine = input("Type 'off' to turn OFF the Machine else type 'no': ")
    if machine=="off":
        clear()
    return machine
#The Actual Functioning starts here!!
print(art.logo)
while machine=="off":
    machine = input("Type 'on' to turn ON the Machine: ")
while machine!="off":

    type = display()
    if type=='report':
        display_report()
    elif type in recipe:
        order = sufficiency_check(type)
        make_payment(order)
        make_coffee(order)
        machine = power()
    else:
        print("Invalid input!!")







