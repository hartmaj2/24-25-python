from __future__ import annotations
from typing import Callable

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
        self.rank = -1  # default value

    def __repr__(self) -> str:
        """
        Returns a simple string representation.
        (Useful when printing the cards in a list. __str__ would not work)

        Returns:
            str: The player's name.
        """
        return self.name

    def comp_rank(self,table : list[Card]):
        cards = self.cards + table
        if check_straight_flush(cards):
            self.rank = 8
        elif check_n_same_pow(cards,4,1):
            self.rank = 7
        elif check_n_same_pow(cards,3,1) and check_n_same_pow(cards,2,1):
            self.rank = 6
        elif check_flush(cards):
            self.rank = 5
        elif check_straight(cards):
            self.rank = 4
        elif check_n_same_pow(cards,3,1):
            self.rank = 3
        elif check_n_same_pow(cards,2,2):
            self.rank = 2
        elif check_n_same_pow(cards,2,1):
            self.rank = 1
        else:
            self.rank = 0

    def __lt__(self, other: Player) -> bool:
        if self.rank == -1 or other.rank == -1:
            raise ValueError
        return self.rank < other.rank

def load_input(filename : str) -> tuple[list[Card],list[Player]]:
    """
    Loads game data from a file.

    Args:
        filename (str): Path to the input file.

    Returns:
        tuple: 
            A tuple containing:
            - A list of Card objects representing the table cards.
            - A list of Player objects representing the players.
    """
    file = open(filename)
    n = int(file.readline())
    table = [Card(s) for s in file.readline().split()]
    players = [Player(file.readline()) for _ in range(n)]
    return table,players

# TODO: copy the following content to a text file and load it from the file using the `load_input`` function
"""
10
8d Jd 9d
Zita 8c 8s
Lubos 4d As
Oliver 9c 2d
Ursula 7s Ts
Jiri Th Qc
Vaclav Td Qd
Silvie Td 2d
Beata 8h Kh
Tatana Jh 9c
Borivoj 4d 5d
"""

table,players = load_input("25_04_25/input.txt")

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

def check_straight_flush(cards : list[Card]):
    if check_flush(cards) and check_straight(cards):
        return True
    return False

"""
10
8d Jd 9d
Zita 8c 8s          THREE OF A KIND
Lubos 4d As         HIGH CARD
Oliver 9c 2d        ONE PAIR
Ursula 7s Ts        STRAIGHT (ENDS WITH Q)
Jiri Th Qc          STRAIGHT (ENDS WITH J)
Vaclav Td Qd        STRAIGHT_FLUSH
Silvie Td 2d        FLUSH
Beata 8h Kh         ONE PAIR
Tatana Jh 9c        TWO PAIRS
Borivoj 4d 5d       FLUSH
"""

for player in players:
    player.comp_rank(table)

players.sort(reverse=True)

for player in players:
    # print(player)
    cards = player.cards + table
    print(f"{player.name:20}{str(cards):20}{player.rank:20}")

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
