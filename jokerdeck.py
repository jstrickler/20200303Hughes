#!/usr/bin/env python
from carddeck import CardDeck

class Game:
    def _make_deck(self):
        pass

    def register_scores(self):
        pass

class JokerDeck(CardDeck, Game, dict):


    def doit(self):
        self._dealer_name = "Fred"

    def _make_deck(self):
        j1 = 'Joker', 1
        j2 = 'Joker', 2

        super()._make_deck()
        self._cards.append(j1)
        self._cards.append(j2)
