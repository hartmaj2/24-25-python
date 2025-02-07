import os

cookies = 0
click_power = 1

# Location: "home", "shop"
location = "home"

# inventory = []
grandmas = 0
grandma_cost = 10
running = True

# 
item_names = ["grandma","turbo oven","grandpa","cookie blaster"]
item_powers = [1,5,10,50]
item_costs = [10,100,500,2000]

inventory = [0,0,0,0]

# DISPLAYING GAME

def clear():
    os.system("clear")

def print_inventory():
    print(20*"-")
    print("Inventory: ")
    for i in range(len(inventory)):
        if inventory[i] != 0:
            print(f"{item_names[i]}: {inventory[i]}")
    print(20*"-")

def print_shop_choices():
    print("Items you can buy:")
    for i in range(len(item_names)):
        print(f"[{i}] - buy {item_names[i]} for {item_costs[i]} with power {item_powers[i]}")
    print("[home] - go home")

def print_home_choices():
    print("Choices you can type: ")
    print("[shop] - go to shop")
    print("[space] - get cookie")
    print("[exit] - exit game")

def display_game():
    print(f"Where you are: {location}")
    print(f"cookies {cookies}:\nclick power: {click_power}")
    print_inventory()
    if location == "shop":
        print_shop_choices()
    elif location == "home":
        print_home_choices()

# PROCESSING GAME 

def process_shop():
    global choice, location, cookies, grandmas, click_power
    if choice == "home":
        location = "home"
    if not choice.isdigit(): # skip all following code if choice is not digit
        return
    i = int(choice)
    if i >= 0 and i < len(item_names): # we choosed some valid item index
        if cookies >= item_costs[i]: # we have enough money to buy that item
            click_power += item_powers[i]
            cookies -= item_costs[i]
            inventory[i] += 1 
            print(f"You bought {item_names[i]}")
            input("Press enter to continue...")
        else:
            print(f"Not enough money for {item_names[i]}!")
            input("Press enter to continue...")


def process_home():
    global choice, location, cookies, running
    if choice == "shop":
        location = "shop"
    elif choice == " ":
        cookies += click_power
    elif choice == "exit":
        running = False


def get_input_message():
    if location == "shop":
        return "Enter shop choice: "
    elif location == "home":
        return "Enter home choice: "

def strip_choice():
    global choice
    if choice != " ":
        choice = choice.strip()

def process_game_step():
    global location, cookies, choice
    choice = input(get_input_message())
    strip_choice()
    if location == "shop":
        process_shop()
    elif location == "home":
        process_home()
    


clear()
display_game()
while running:
    process_game_step()
    clear()
    display_game()
print("Goodbye!")