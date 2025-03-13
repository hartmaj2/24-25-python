from __future__ import annotations

import random

class Card:

    values = "23456789TJQKA" # the order of vals in this string is important
    suits = "shdc" # spades, hearts, diamonds, clubs
    
    # initializes card received in format "Xs" where X is char corresponding to card value and s char corresponding to suit
    def __init__(self,card_string : str):
        v = card_string[0]
        s = card_string[1]

        self.value = v
        self.power = Card.values.index(self.value)
        self.suit = s

    #  PRINTING
    def __str__(self):
        return f"{self.value}{self.suit}"
    
    # COMPARISONS
    def __eq__(self,other : Card):
        return self.power == other.power
    
    def __lt__(self, other : Card):
        return self.power < other.power

    def __le__(self, other : Card):
        return self < other or self == other
    
    def __gt__(self, other : Card):
        return not self <= other

    def __ge__(self, other : Card):
        return self > other or self == other


    

cards = []

for suit in Card.suits:
    for value in Card.values:
        cards.append(Card(value + suit))

random.shuffle(cards)

cards.sort()

for card in cards:
    print(card)


