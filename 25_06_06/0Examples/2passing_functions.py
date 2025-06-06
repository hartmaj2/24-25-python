# Passing functions can be especially useful for our player class
# we can pass a function that selects exactly what we want from the current player

from typing import Callable

class Player:
    def __init__(self, name, team, nationality, position):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.position = position

    def __repr__(self):
        return self.name

def select_nationality(player : Player) -> str:
    return player.nationality

def select_team(player : Player) -> str:
    return player.team

def guess_attribute(player : Player, selector : Callable[[Player],str], attr_name : str):
    print(f"What is the {attr_name} of {player}")
    answer = input("Enter your answer: ")
    correct = selector(player)
    if answer.lower() == correct.lower():
        print("Good job!")
    else:
        print(f"No, the correct answer is {correct}")

messi = Player("Lionel Messi","Barcelona","Argentina","Forward")

guess_attribute(messi,select_nationality,"nationality")

guess_attribute(messi,select_team,"team")