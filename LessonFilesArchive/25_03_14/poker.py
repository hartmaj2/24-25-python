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

def check_straight(cards : list[Card]) -> bool:
    cards.sort(reverse=True)
    firstval = cards[0].power
    for i in range(len(cards)):
        if cards[i].power != firstval - i:
            return False
    return True

def count_n_of_kind(cards : list[Card], n : int) -> int:
    cards.sort(reverse=True)
    count = 0
    active_power = cards[0].power
    repetitions = 1 # we have every time at least one same card to each other
    for i in range(1,len(cards)):
        if cards[i].power == active_power: # the next card has same power as the active power
            repetitions += 1
        else: # suddenly, we have a new card power (lower), so we reset the counter and start again
            active_power = cards[i].power
            repetitions = 1 
        if repetitions == n: # check if we have not encountered n same cards in a row
            count += 1
    return count

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
    def __str__(self) -> str:
        return f"{self.value}{self.suit}"
    
    # COMPARISONS
    def __eq__(self,other : Card) -> bool:
        return self.power == other.power
    
    def __lt__(self, other : Card) -> bool:
        return self.power < other.power

    def __le__(self, other : Card) -> bool:
        return self < other or self == other
    
    def __gt__(self, other : Card) -> bool:
        return not self <= other

    def __ge__(self, other : Card) -> bool:
        return self > other or self == other

class Player:

    def __init__(self, player_string : str):
        name, card1, card2 = player_string.split()
        self.name = name
        self.cards = [Card(card1),Card(card2)]

    def __str__(self) -> str:
        return self.name

    # evaluation vector will be 6-tuple where the components of the tuple from left to right denote powers at different comparison levels
    # (explain sorting using multiple runs going from the most specific to least specific tie breaking component)
    def evaluate_hand(self, table_cards : list[Card]):
        ...

# loads the input and returns a list of cards on table and list of players
def load_input(filename : str) -> tuple[list[Card],list[Player]]:
    file = open(filename)
    num_players = int(file.readline())
    table_cards = create_table_cards(file.readline())
    players = []
    for _ in range(num_players):
        players.append(Player(file.readline()))
    file.close()
    return table_cards, players

# given a string of table cards creates the list of those cards
def create_table_cards(table_cards_string : str) -> list[Card]:
    table_cards = []
    for card_string in table_cards_string.split():
        table_cards.append(Card(card_string))
    return table_cards    

# DEBUG: creates a deck of all possible cards
def create_card_deck() -> list[Card]:
    cards = []
    for suit in Card.suits:
        for value in Card.values:
            cards.append(Card(value + suit))
    return cards

# given a list of cards prints a string corresponding to the card combination
def combination_string(cards) -> str:
    return " ".join([str(card) for card in cards])

input_filename = "input.txt"
table_cards, players = load_input(input_filename)

for player in players:
    combination = table_cards + player.cards
    combstring = combination_string(combination)
    res = count_n_of_kind(combination,3)
    print(f"{player!s:10}: {combstring:20} has straight: {res:10}")