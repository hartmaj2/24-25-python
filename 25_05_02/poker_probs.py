# This program should test what are the probabilities of getting certain combinations in poker
# will test this by simulation

from __future__ import annotations
from typing import Callable

import random

# Starter kit to solve the following: https://ksp.mff.cuni.cz/z/ulohy/37/zadani4.html#task-37-Z4-2:~:text=37%2DZ4%2D2%20Poker%20(10%20bod%C5%AF)

class Card:
    """
    Represents a standard playing card.

    Attributes:
        value (str): value of the card as string symbol
        power (int): power of the card
        suit (str): suit of the card
    """

    VALUES = "23456789TJQKA"
    SUITS = "cdhs"

    def __init__(self, card_string: str):
        """
        Initializes a card from a string.

        Args:
            card_string (str): A 2-character string where the first character is the card value 
                               and the second is the suit (e.g., 'As' for Ace of Spades).
        """
        v = card_string[0]
        s = card_string[1]

        self.value = v  #: str: The card's value symbol (e.g., 'A', 'K', '2').
        self.power = Card.VALUES.index(self.value)  #: int: The power of the card used for comparison.
        self.suit = s  #: str: The suit of the card (e.g., 's' for spades).

    def __repr__(self) -> str:
        """
        Returns string representation of the card. 
        (Useful when printing the cards in a list. __str__ would not work)

        Returns:
            str: The card's string form (e.g., 'As').
        """
        return f"{self.value}{self.suit}"

    def __lt__(self, other: Card) -> bool:
        """
        Compares two cards based on their power.

        Args:
            other (Card): The card to compare against.

        Returns:
            bool: True if self is less powerful than other.
        """
        return self.power < other.power

class Player:
    """
    Represents a poker player with a name, hand cards, and hand value.

    Attributes:
        name (str): Name of the player.
        cards (list of Card): List of two cards the player has in hand.
        value (int): Evaluated hand value; default is -1.
    """

    def __init__(self, player_string: str):
        """
        Initializes a player from a string.

        Args:
            player_string (str): String in format "Name Card1 Card2" (e.g., "John As 4c").
        """
        name, card1, card2 = player_string.split()
        self.name = name
        self.cards = [Card(card1), Card(card2)]
        self.value = -1  # default value

    def __repr__(self) -> str:
        """
        Returns a simple string representation.
        (Useful when printing the cards in a list. __str__ would not work)

        Returns:
            str: The player's name.
        """
        return self.name

    def evaluate_hand(self, table_cards: list[Card]):
        """
        Evaluates the player's hand value based on table cards.

        Args:
            table_cards (list of Card): Community cards on the table.
        """
        ...
        # TODO: implement this function

    def __lt__(self, other: 'Player'):
        """
        Compares two players by their evaluated hand value.

        Args:
            other (Player): The other player to compare with.

        Returns:
            bool: True if self's hand value is less than other's.
        """
        return self.value < other.value


# checks whether the cards are in increasing order when sorted
def check_straight(cards : list[Card]):
    cards_c = cards.copy()
    cards_c.sort()
    frst_pow = cards_c[0].power
    i = 0
    for card in cards_c:
        if card.power != frst_pow + i:
            return False
        i += 1
    return True

# checks whether all cards are of the same suit
def check_flush(cards : list[Card]):
    suit_first = cards[0].suit
    for card in cards:
        if card.suit != suit_first:
            return False
    return True

# checks whether there are n cards with same power
# optionally, using the last parameter, we can check if there are exactly k different groups of n same cards
def check_n_same_pow(cards : list[Card], n : int, k : int = 1) -> bool:
    buckets = get_buckets(cards)
    for i in range(n,5):
        if buckets.count(i) >= k:
            return True
    return False


# checks whether there are exactly n cards with same power
# optionally, using the last parameter, we can check if there are exactly k different groups of n same cards
def check_exactly_n_same_pow(cards : list[Card], n : int, k : int = 1) -> bool:
    buckets = get_buckets(cards)
    if buckets.count(n) == k:
            return True
    return False

# creates a sequence of buckets
# the buckets are labeled by power of cards an count how many cards of that power are in the cards list
def get_buckets(cards : list[Card]) -> list[int]:
    buckets = len(Card.VALUES) * [0]
    for card in cards:
        buckets[card.power] += 1

    return buckets

# tests the function check_func on all the players and the table given
def test(players : list[Player], table : list[Card], rank_func : Callable[[list[Card]],int]):
    for player in players:
        cards = player.cards + table
        print(f"{player.name:20}{rank_to_string(rank_func(cards)):20}")

# given the cards, returns the rank of the combination (higher rank means more powerful combination)
# RANK:
# 8 <- straight flush
# 7 <- quadruple
# 6 <- full house
# 5 <- flush
# 4 <- straight
# 3 <- triple
# 2 <- two pairs
# 1 <- one pair
# 0 <- high card
def compute_comb_rank(cards : list[Card]) -> int:
    if check_flush(cards) and check_straight(cards):
        return 8
    elif check_n_same_pow(cards,4):
        return 7
    elif check_n_same_pow(cards,3) and check_n_same_pow(cards,2):
        return 6
    elif check_flush(cards):
        return 5
    elif check_straight(cards):
        return 4
    elif check_n_same_pow(cards,3):
        return 3
    elif check_n_same_pow(cards,2,2):
        return 2
    elif check_n_same_pow(cards,2):
        return 1
    else:
        return 0


RANK_TO_STR = ["high card","one pair","two pairs","triple","straight","flush","full house","quadruple","straight flush"]

# smarter would be to use Enum but for educational purposes to not introduce too much new stuff, we use this mapping instead
def rank_to_string(rank : int) -> str:
    return RANK_TO_STR[rank]


deck = []
for suit in Card.SUITS:
    for value in Card.VALUES:
        deck.append(Card(value + suit))

# TODO: fix two pairs (full house should also be two pairs)
def get_checks_vect(cards : list[Card]) -> list[int]:
    checks_vect = [0] * len(RANK_TO_STR)
    if check_flush(cards) and check_straight(cards):
        checks_vect[8] = 1
    if check_n_same_pow(cards,4):
        checks_vect[7] = 1
    if check_exactly_n_same_pow(cards,3) and check_exactly_n_same_pow(cards,2):
        checks_vect[6] = 1
    if check_flush(cards):
        checks_vect[5] = 1
    if check_straight(cards):
        checks_vect[4] = 1
    if check_n_same_pow(cards,3):
        checks_vect[3] = 1
    if check_n_same_pow(cards,2,2):
        checks_vect[2] = 1
    if check_n_same_pow(cards,2):
        checks_vect[1] = 1
    checks_vect[0] = 1
    return checks_vect

probabilities = len(RANK_TO_STR) * [0]
trials = 1_000_000
for i in range(trials):
    random.shuffle(deck)
    cards = deck[:5]
    checks_vect = get_checks_vect(cards)
    probabilities = list(map(lambda x,y : x + y,probabilities,checks_vect))
print(probabilities)

"""
How to calculate these probabilities:

possible card combination
    - nCr(52,5)

straight
    - a = 9 possible ways a straight can begin (when we imagine the cards sorted)
    - each card can have 4 colors -> b = 4^5
    - res = a * b

flush 
    - a = 4 possible colors
    - b = nCr(13,5) possible sets of card values
    - res = a * b

straight flush
    - a = 9 -||- (see straight)
    - b = 4 possible colors
    - res = a * b

quadruple
    - quadruple is fixed
    - a = 13 possible values the quadrupled card can have
    - b = 48 possible other cards to pick
    - res = a * b

triple
    - a = 4 ways to pick the colors of the triple (one color always missing)
    - b = 13 ways to pick the value of the triple
    - c = nCr(48,2) ways to pick the rest of the cards
    - res = a * b * c + quadruples

two pair 
    - a_1 = nCr(4,2) ways to pick colors of the first pair
    - !!! a_2 = nCr(4,2) ways to pick colors of the second pair
    - b = nCr(13,2) ways to pick the values of the pairs
    - c = 48 ways to pick the last card
    - res = a_1 * a_2 * b * c

"""