# TODO: Zamyslet se nad obecnym navrhem hry nez zacneme programovat.
# 1. Nakreslit si schema TYPU veci, ktere se ve hre vyskytuji a jake maji vlastnosti (hra samotna, hrac, obchod, predmet)
# 2. Jakym zpusobem bude hra komunikovat s hracem (mackani enteru asi, jak se bude vykreslovat vysledek?)

# Game loop pattern - input, update, draw
# GAME_STATE -> in_clicker; in_shop

import os

MAIN_SCREEN = "in_clicker"
IN_SHOP = "in_shop"
GAME_OVER = "game_over"
JUST_CLICKED = "just_clicked"

GRANDMA = "grandma"
TURBO_OVEN = "turbo oven"
SHOP_ITEMS = [GRANDMA,TURBO_OVEN]

# simplest version
ITEM_PRICES = [10,20]
ITEM_BOOSTS = [1,2]


# better version (dictionary)
ITEM_PRICES2 = {GRANDMA : 10, TURBO_OVEN : 20}
ITEM_BOOSTS2 = {GRANDMA : 1, TURBO_OVEN : 2}

inventory2 = {}

def clear_screen():
    os.system("clear")

def press_enter_to_continue():
    global game_state
    if game_state != JUST_CLICKED and game_state != GAME_OVER:
        input("Press enter to continue...")


def print_choices():
    if game_state == MAIN_SCREEN or game_state == JUST_CLICKED:
        print("Just press space to earn money!")
        print("0. - exit game")
        print("1. - go to shop")
    elif game_state == IN_SHOP:
        print("Just press space to exit")
        for i in range(len(SHOP_ITEMS)):
            print(f"{i}. {SHOP_ITEMS[i]}, price: {ITEM_PRICES[i]}, boost: {ITEM_PRICES[i]}")


def print_inventory():
    printed_names = []
    printed_counts = []
    for item in inventory:
        if item not in printed_names:
            printed_names.append(item)
            printed_counts.append(1)
        else:
            printed_counts[printed_names.index(item)] += 1
    print(10*"-")
    print("Inventory: ")
    for i in range(len(printed_names)):
        print(f"{printed_names[i]}: {printed_counts[i]}")
    print(10*"-")




def process_shop_choice():
    global points, choice, game_state
    if not choice.isnumeric():
        print("Exitting the shop")
        game_state = MAIN_SCREEN
        return
    i = int(choice)
    if i < 0 or i >= len(SHOP_ITEMS):
        print("Invalid shop choice")
        return
    item_name = SHOP_ITEMS[i]
    item_price = ITEM_PRICES[i]
    if item_price > points:
        print(f"You are too poor to buy {item_name}")
        return 
    points -= item_price
    inventory.append(item_name)
    print(f"You succesfuly bought {item_name}")



def process_main_screen_choice():
    global choice, points, game_state
    if choice == "":
        game_state = JUST_CLICKED
        points += calculate_points_gain()
    elif choice == "0":
        print("Goodbye")
        game_state = GAME_OVER
    elif choice == "1":
        print("You went to the shop")
        game_state = IN_SHOP



def calculate_points_gain():
    points_gain = 1
    for item in inventory:
        points_gain += ITEM_BOOSTS[SHOP_ITEMS.index(item)]
    return points_gain


def process_choice():
    global choice, points, game_state

    if game_state == MAIN_SCREEN or game_state == JUST_CLICKED:
        process_main_screen_choice()  
    elif game_state == IN_SHOP:
        process_shop_choice()


def print_player():
    print(20*"-")
    print(f"Points: {points}")
    print(f"Click power {calculate_points_gain()}")
    print_inventory()
    print(20*"-")

def load_player_choice():
    global choice
    choice = input("Enter your choice: ")

inventory = []
game_state = MAIN_SCREEN
points = 0
choice = ""
while game_state != GAME_OVER:
    clear_screen()
    print_player()
    print_choices()
    load_player_choice()
    process_choice()
    press_enter_to_continue()