# Demonstrates that code will be run before we get to the error

items = ["book of wisdom","magical banana","staff of power"]

item_powers = [10,5,43]

print("The items are getting older and they are slowly losing their original power.") # this will be printed

value = input("Enter some value please: ")

for i in range(len(items)):
	items[i] -= 1

for i in range((len(items))):
	print(f"{items[i]}\t{item_powers[i]}")