from __future__ import annotations



class Card:

    dictonary = {"A" : 14, "K" : 13, "Q" : 12, "J" : 11, "T" : 10}
    
    def __init__(self,v,s):
        if v in Card.dictonary:
            self.value = Card.dictonary[v]
        else:
            self.value = v
        self.suit = s

    def __str__(self):
        return f"Card: value - {self.value}, color - {self.suit}"

    def is_bigger_than(self, card2 : Card):
        return self.value > card2.value
    
    def equals(self,card2 : Card):
        return self.value == card2.value

class Item:

    def __init__(self,name,price,damage):
        self.name = name
        self.price = price
        self.damage = damage


item = Item("sekera",10,100)
# seznam = [Card("A","d"),Card("A","d"),Card("A","d"),Card("A","d"),Card("A","d")]

# print(slovnik["K"])

# karta3 = Card("Td","sdf")
karta = Card("K","d")
karta2 = Card("A","c")
print(karta)

# Card.is_bigger_than()
# if karta.is_bigger_than(karta2):
#     print("Karta je vetsi nez karta2")

# if karta.equals(karta2):
#     print("Karta ma stejnou hodnotu jako ta druha")

# print(karta2)
# if karta.is_bigger_than(karta2) :
    # ...

# karta.is_bigger_than(karta2)

# print(karta.suit)
# print(karta2.suit)

# print(karta.value)
# print(karta2)