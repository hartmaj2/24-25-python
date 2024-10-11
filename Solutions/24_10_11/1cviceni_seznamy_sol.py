# TODO: 
# nize mas seznam itemu, ktere nabizi obchod 
store_items = ["mana potion","sword","armor","shield"]

# tvuj inventar
inventory = []

def print_store_items():
    print("Items in store: ")
    for i in range(len(store_items)):
        print(f"  {i+1}. {store_items[i]}") 

def print_inventory():
    print("Inventory: ",end=" ")
    print(inventory)

# TODO: vypis vsechny predmety, ktere obchod nabizi

# OCEKAVANY VYSTUP PROGRAMU:
# Items in store:
#   1. mana potion
#   2. sword
#   3. armor
#   4. shield

print()
print_inventory()
print("Items in store: ")
for i in range(len(store_items)):
    print(f"  {i+1}. {store_items[i]}")


# TODO: kup si druhy predmet tim
# 1. odeberes ten predmet ze seznamu predmetu `store_items` a pridas do sveho
# 2. pridas tento predmet do seznamu `inventory`
# POZOR: tvuj program by mel fungovat i v pripade, ze v obchodu budou uplne jine predmety

# print("\nTED SI NECO KOUPIM\n")

# item = store_items[1]
# store_items.remove(item)
# inventory.append(item)

# print_store_items()
# print_inventory()

# TODO: Nech uzivatele zvolit cislo predmetu, ktery chce koupit a pridej mu ten predmet do inventare

volba = input("\nZadej cislo predmetu: ")
item = store_items[int(volba)-1]
store_items.remove(item)
inventory.append(item)

print()
print_inventory()
print_store_items()

# BONUS: hezky design tohoto programu by byl takovy, 
# ze pro vytisknuti veci v obchode bychom si napsali funkci
# tim padem budeme moct opakovane pouzivat tuto funkci
# a nemusime tedy psat cely kod, ktery funkce provadi znovu a znovu

