items = []

item_powers = []

print("The items are getting older and they are slowly losing their original power.") # this will be always printed

for i in range(len(items)):
	items[i] -= 1

for i in range((len(items))):
	print(f"{items[i]}\t{item_powers[i]}")