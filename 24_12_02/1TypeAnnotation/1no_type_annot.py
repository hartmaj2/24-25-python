items = ["book of wisdom","magical banana","staff of power"]

item_powers = [10,5,43]

# is called when the node appears in the game
def _ready():

	# the items are getting older and weaker with time
	for i in range(len(items)):
		items[i] -= 2
		
_ready()