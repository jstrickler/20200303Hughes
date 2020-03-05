#!/usr/bin/env python
import random

class CardDeck:
    SUITS = 'C D H S'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self._dealer_name = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

#    @property
    def dealer_name(self): # getter property
        return self._dealer_name

    dealer_name = property(dealer_name)

    @dealer_name.setter
    def dealer_name(self, dealer):
        if isinstance(dealer, str):
            self._dealer_name = dealer
        else:
            raise TypeError("Dealer must be a string, my friend")

# @foo
# def bar():
#     pass
#
# bar = foo(bar)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    def __len__(self):
        return len(self._cards)


    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({len(self)})"

    def __add__(self, other):
        my_type =type(self)
        tmp = my_type(self.dealer_name)
        tmp._cards = self.cards + other.cards
        return tmp


# len(x)
# x.__len__()
# str(x)
# x.__str__()
