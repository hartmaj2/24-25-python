from __future__ import annotations

hodnoty = "23456789TJQKA"

class Card:

    def __init__(self,card_string : str):
        self.value = card_string[0]
        self.power = hodnoty.index(self.value)
        self.suit = card_string[1]

    def __lt__(self,other : Card):
        if self.power < other.power:
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self.value} {self.suit}"

# karta = Card("Ks")
# karta2 = Card("2h")
# kral = Card("Ks")
# eso = Card("Ah")

Card("Ak")
# if kral < eso:
#     print("kral mensi")

string = "Xita As Kh"

print(string.split())

karty = []


