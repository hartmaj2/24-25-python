from __future__ import annotations

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

def pair(karty : list[Card]):
    powers = []
    for card in karty:
        powers.append(card.power)
    print(f"Vznikl tento seznam: {powers}")

def get_buckets(karty : list[Card]) -> list[int]:
    buckets = len(Card.VALUES) * [0]
    for card in karty:
        buckets[card.power] += 1

    return buckets

karty = table + players[0].cards

pair(karty)

print(get_buckets(karty))

# print(get_buckets(karty))
# pair()
# TODO: try to print players and table cards

# TODO: print what cards Lubos has

# TODO: print powers and suits of the cards on the table