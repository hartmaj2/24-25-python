# I want to print the items sorted based on their costs from the cheapest one going up

def print_items():
    print("ITEMS:")
    for item in items:
        print(f"{item.name}\tprice: {item.cost}\tpower: {item.power}")
    print()

class Item:
    def __init__(self,name,cost,power):
        self.name = name
        self.cost = cost
        self.power = power

items = [Item("sword",10,23), Item("shield",5,10), Item("helmet",20,4), Item("staff",4,5)]

items.sort(key = lambda it : it.cost)

print_items()

items.pop(2)

print_items()