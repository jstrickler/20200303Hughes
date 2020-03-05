#!/usr/bin/env python
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Anne")
print(d1)

d2 = CardDeck("Fernando")
print(d2)

print(d1.dealer_name)
print(d2.dealer_name)

d1.dealer_name = "Bob"

print(d1.dealer_name)

try:
    d1.dealer_name = 123.456
except TypeError as err:
    print(err)

print(d1.dealer_name)
print(d1.dealer_name.upper())

d1.shuffle()
print(d1.cards, '\n')

for i in range(7):
    print(d1.draw())

print(d1.get_ranks())

print(CardDeck.get_ranks())
print("=" * 40)
j1 = JokerDeck("Beulah")
print(j1)
j1.shuffle()
print(j1.cards)

print(JokerDeck.mro())
j1.register_scores()

j1.doit()
print(j1.dealer_name)

print(len(d1),len(j1))


print(dir(object))
import sys
print(sys.getsizeof(object))
print(sys.getsizeof(j1))

print(d1, j1)

new_deck = d1 + j1
print(new_deck)
print(len(new_deck))
