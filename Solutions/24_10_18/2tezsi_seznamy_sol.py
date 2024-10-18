import os

# TODO: 
# nize mas seznam itemu, ktere nabizi obchod a pod nim seznam jejich cen ve stejnem poradi
store_items = ["potion","sword","armor","shield"]
store_items_prices = [10,5,13,17]

# tvuj inventar a seznam cen predmetu v tvem inventari (zatim nic nemas)
inventory = []
inventory_prices = []

# pocet penez, ktere mas k dispozici
money = 15

def print_items(text : str, items : list[str], prices : list[int]):
    print(text)
    for i in range(len(items)):
        print(f"  {i+1}. {items[i]}\t{prices[i]}")

def print_store():
    print_items("Items in store: ",store_items,store_items_prices)

def print_inventory():
    print_items("Inventory: ",inventory,inventory_prices)

def print_player():
    print(f"Money: {money}")
    print_inventory()
    print_inventory_value()

def print_inventory_value():
    sum = 0
    for price in inventory_prices:
        sum += price
    print(f"Value of your inventory is: {sum}")

# TODO: vypis vsechny predmety, ktere obchod nabizi a jejich ceny
# Items in store: 
#   1. potion     10
#   2. sword      5
#   3. armor      13
#   4. shield     17

# print_store()
# print_player()

# TODO: nech uzivatele zvolit poradi predmetu, ktery chce koupit a pridej mu ten predmet do inventare
# POZOR: predmet lze koupit pouze pokud ma hrac dost penez
# HINT: nezapomen hraci odecist penize

# index = int(input("Jaky predmet si chces koupit: ")) - 1
# if store_items_prices[index] > money:
#     print("Na to, abys koupil tento predmet jsi moc velky chudak.")
# else:
#     item, price = store_items[index], store_items_prices[index]
#     money -= price
#     inventory.append(item)
#     inventory_prices.append(price)
#     store_items.remove(item)
#     store_items_prices.remove(price)

# print_store()
# print_player()

# TODO: pridej i moznost buy a sell
# 1. zeptej se uzivatele, zda chce kupovat nebo prodavat
# 2. podle jeho volby:
    # pokud si zvolil nakup -> zobraz seznam predmetu v obchode
    #   ...          prodej -> zobraz seznam predmetu z inventare

def buy():
    global money
    print_store()
    volba = input("Which item do you want to buy? ")
    if not volba.isnumeric():
        print("Invalid choice")
        return 
    volba = int(volba)
    if volba >= 1 and volba <= len(store_items):
        if store_items_prices[volba-1] <= money:
            item,price = store_items[volba-1], store_items_prices[volba-1]
            money -= price
            store_items.remove(item)
            store_items_prices.remove(price)
            inventory.append(item)
            inventory_prices.append(price)
            print(f"You bought {item} for {price} dollars")
        else:
            print("You are too poor to buy this")
    else:
        print("Invalid choice")

def sell():
    global money
    if len(inventory) == 0:
        print("You don't have anything to sell")
        return
    print_inventory()
    volba = input("Which item do you want to sell? ")
    if not volba.isnumeric():
        print("Invalid choice")
        return 
    volba = int(volba)
    if volba >= 1 and volba <= len(inventory):
        item,price = inventory[volba-1], inventory_prices[volba-1]
        money += price
        inventory.remove(item)
        inventory_prices.remove(price)
        store_items.append(item)
        store_items_prices.append(price)
        print(f"You sold {item} for {price} dollars")
    else:
        print("Invalid choice")


volba = 0
while volba != -1:
    os.system("clear")
    volba = input("Buy (1), sell (2) or show info (3)? ")
    if not volba.isnumeric():
        print("Invalid choice")
        continue
    volba = int(volba)
    os.system("clear")
    if volba == 1:
        buy()
        input()
    if volba == 2:
        sell()
        input()
    if volba == 3:
        print_player()
        input()
    

# BONUS2 TODO: pridej moznost nechat si vypsat celkovou hodnotu vsech veci ve tvem inventari





