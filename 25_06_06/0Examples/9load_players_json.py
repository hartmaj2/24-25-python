# Example of how to load players using json

# Since the loaded data for each player is a dictionary, we need to have a function that creates a Player from a dict

import json

from player import Player

file = open("25_06_06/players.json")
p_dicts = json.load(file)

players = []

for p_dict in p_dicts:
    players.append(Player.load_from_dict(p_dict))

print(players)
