var items : Array[String] = ["book of wisdom","magical banana","staff of power"]

var item_powers : Array[int] = [10,5,43]

# is called when the node appears in the game
func _ready():
	
	# the items are getting older and weaker with time
	for i in range(len(items)):
		items[i] -= 2