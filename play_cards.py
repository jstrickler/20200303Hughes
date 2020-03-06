#!/usr/bin/env python
"""
Main program for playing cards
"""
import sys
import time
from carddeck import CardDeck
from jokerdeck import JokerDeck

start = time.time()

D1 = CardDeck("Anne")
print(D1)

D2 = CardDeck("Fernando")
print(D2)

print(D1.dealer_name)
print(D2.dealer_name)

D1.dealer_name = "Bob"

print(D1.dealer_name)

try:
    D1.dealer_name = 123.456
except TypeError as err:
    print(err)

print(D1.dealer_name)
print(D1.dealer_name.upper())

D1.shuffle()
print(D1.cards, '\n')

for i in range(7):
    print(D1.draw())

print(D1.get_ranks())

print(CardDeck.get_ranks())
print("=" * 40)
J1 = JokerDeck("Beulah")
print(J1)
J1.shuffle()
print(J1.cards)

print(JokerDeck.mro())
J1.register_scores()

J1.doit()
print(J1.dealer_name)

print(len(D1), len(J1))


print(dir(object))
print(sys.getsizeof(object))
print(sys.getsizeof(J1))

print(D1, J1)

NEW_DECK = D1 + J1
print(NEW_DECK)
print(len(NEW_DECK))

end = time.time()

print(f"Total elapsed time: {round(end - start, 9)} seconds")
