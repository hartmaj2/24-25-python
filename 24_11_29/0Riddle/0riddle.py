# I want to print the items sorted based on their costs from the cheapest one going up

items = ["sword","shield","helmet","staff"]
item_costs = [10,5,20,4]
item_powers = [23,10,4,5]

item_costs.sort()

for i in range(len(items)):
    print(f"{items[i]}\tprice: {item_costs[i]}\tpower: {item_powers[i]}")

# is this correct? how to do this correctly?