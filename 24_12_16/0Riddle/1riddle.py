# Riddle: what will this piece of code do?
# Exactly describe what the program will output.

items = ["book of wisdom","magical banana","staff of power"]

item_powers = [10,5,43]

print("The items are getting older and they are slowly losing their original power.")

for i in range(len(items)):
	items[i] -= 1

for i in range((len(items))):
	print(f"{items[i]}\t{item_powers[i]}")