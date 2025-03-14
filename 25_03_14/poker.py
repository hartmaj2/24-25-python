from __future__ import annotations
from enum import Enum, auto

import random

# poker combinations
class Combination(Enum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIRS = auto()
    THREE_OF_KIND = auto()
    STRAIGHT = auto()
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_OF_KIND = auto()
    STRAIGHT_FLUSH = auto()

# combinations evaluation
def check_flush(cards : list[Card]) -> bool:
    suit = cards[0].suit
    for card in cards:
        if card.suit != suit:
            return False
    return True

def check_straight(cards : list[Card]):
    cards.sort(reverse=True)
    firstval = cards[0].power
    for i in range(len(cards)):
        if cards[0].power != firstval + i:
            return False
    return True

def check_n_of_kind(cards : list[Card], n : int):
    cards.sort(reverse=True)
    active_power = card[0]
    amount_same = 1 # we have every time at least one same card to each other
    for i in range(1,len(cards)):
        if amount_same == n: # check if we have not encountered n same cards in a row
            return True
        if cards[i].power == active_power: # the next card has same power as the active power
            amount_same += 1
        else: # suddenly, we have a new card power (lower), so we reset the counter and start again
            active_power = cards[i].power
            amount_same = 1 

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

class Player:

    def __init__(self, name : str, cards : list[Card]):
        self.name = name
        self.cards = cards

    def __str__(self):
        print(f"{self.name}")

    # evaluation vector will be 6-tuple where the components of the tuple from left to right denote powers at different comparison levels
    # (explain sorting using multiple runs going from the most specific to least specific tie breaking component)
    def evaluate_hand(self, table_cards : list[Card]):
        ...




cards = []

for suit in Card.suits:
    for value in Card.values:
        cards.append(Card(value + suit))

random.shuffle(cards)

cards.sort()

for card in cards:
    print(card)

# TODO: test the functions for combination evaluation