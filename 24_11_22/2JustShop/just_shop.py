import os

# How to implement a nice shop using lists

# 1. Think of having the table of items

#                   0             1            2               3
# | item_name | "grandma" | "turbo oven" | "grandpa" | "cookie blaster"  |
# | --------- | --------- | ------------ | --------- | ----------------- |
# |   cost    |     10    |     100      |    500    |       2000        |
# |   power   |     1     |      5       |     10    |        50         |

# The index is something like a unique ID of the item
# when we get hold of the id -> we can find in the table all information about the item

item_names = ["grandma","turbo oven","grandpa","cookie blaster"]
item_costs = [10,100,500,2000]
item_powers = [1,5,10,50]

# TODO 1: print just the second item in the shop -> name and cost

# TODO 2: print an item based on choice of user

# TODO 3: print all the items in the shop with their costs

money = 10

# TODO 4: let user choose an item and then tell him if he has enough money to buy it

#                   0             1            2               3
# | item_name | "grandma" | "turbo oven" | "grandpa" | "cookie blaster"  |
# | --------- | --------- | ------------ | --------- | ----------------- |
# |   cost    |     10    |     100      |    500    |       2000        |
# |   power   |     1     |      5       |     10    |        50         |

# inventory just says, how many times the player owns that item

# | inventory |     1     |      4       |     5     |         0         |

inventory = [1,4,5,0] # inventory with some stuff in it

# TODO 5: print player inventory

inventory = [0,0,0,0] # empty inventory

# trick: inventory = [0] * len(item_names)

# TODO 6: start with empty inventory, let player buy some things and add them to inventory