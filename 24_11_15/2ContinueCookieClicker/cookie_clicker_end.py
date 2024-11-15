import os

cookies = 0
click_power = 0

# Location: "home", "shop"
location = "home"

# inventory = []
grandmas = 0


def clear():
    os.system("clear")

def print_inventory():
    print(20*"-")
    print("Inventory: ")
    print(f"Grandmas: {grandmas}")
    print(20*"-")

def print_shop():
    print("Type grandma to buy grandma")

def print_stats():
    print(f"Where you are: {location}")
    print(f"cookies {cookies}:\nclick power: {click_power}")
    print_inventory()
    if location == "shop":
        print_shop()


def process_shop():
    global choice, location, cookies, grandmas
    if choice == "home":
        location = "home"
    elif choice == "grandma":
        grandmas += 1

def process_home():
    global choice, location, cookies
    if choice == "shop":
        location = "shop"
    elif choice == " ":
        cookies += 1


def process_choice():
    global location, cookies, choice

    if location == "shop":
        choice = input("Enter shop choice: ")
    elif location == "home":
        choice = input("Enter a space to get cookies...")

    if location == "shop":
        process_shop()
    elif location == "home":
        process_home()
    


clear()
print_stats()
while True:
    process_choice()
    clear()
    print_stats()
