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

    def __lt__(self,other : Combination):
        return self.value < other.value

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

def get_counts(cards : list[Card]) -> list[int]:
    counts = [0 for i in range(len(Card.values))]
    for card in cards:
        counts[card.power] += 1
    return counts

def get_score(cards: list[Card]) -> Combination:
    flush = check_flush(cards)
    straight = check_straight(cards)
    counts = get_counts(cards)
    if straight and flush:
        return Combination.STRAIGHT_FLUSH
    if 4 in counts:
        return Combination.FOUR_OF_KIND
    if 3 in counts and 2 in counts:
        return Combination.FULL_HOUSE
    if flush:
        return Combination.FLUSH
    if straight:
        return Combination.STRAIGHT
    if 3 in counts:
        return Combination.THREE_OF_KIND
    if counts.count(2) == 2:
        return Combination.TWO_PAIRS
    if 2 in counts:
        return Combination.ONE_PAIR
    else:
        return Combination.HIGH_CARD

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
    
    def __repr__(self) -> str:
        return self.__str__()
    
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
        self.value = None

    def __str__(self) -> str:
        return self.name

    # evaluation vector will be 6-tuple where the components of the tuple from left to right denote powers at different comparison levels
    # (explain sorting using multiple runs going from the most specific to least specific tie breaking component)
    def evaluate_hand(self, table_cards : list[Card]):
        self.value = get_score(self.cards + table_cards)

    def __lt__(self,other):
        return self.value < other.value

# loads the input and returns a list of cards on table and list of players
def load_input(filename : str) -> tuple[list[Card],list[Player]]:
    file = open(filename)
    num_players = int(file.readline())
    table_cards = [Card(c) for c in file.readline().split()]
    players = [Player(file.readline()) for _ in range(num_players)]
    file.close()
    return table_cards, players

# DEBUG: creates a deck of all possible cards
def create_card_deck() -> list[Card]:
    cards = []
    for suit in Card.suits:
        for value in Card.values:
            cards.append(Card(value + suit))
    return cards

input_filename = "input.txt"


def just_print_combs(input_filename):
    table_cards, players = load_input(input_filename)
    for player in players:
        combination = table_cards + player.cards
        res = get_score(combination)
        print(f"{player!s:10}: {combination} {"":10} has straight: {res:10}")

def sort_using_combs(input_filename):
    table_cards, players = load_input(input_filename)
    for player in players:
        player.evaluate_hand(table_cards)
    players.sort(reverse=True)
    for player in players:
        print(f"{player!s:10}: {table_cards + player.cards} {"":10} has straight: {player.value:10}") 

sort_using_combs(input_filename)