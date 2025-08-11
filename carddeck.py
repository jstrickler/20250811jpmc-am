"""
Provide CardDeck class
"""
import random
from card import Card

class CardDeck:
    """
    Represent one deck of 52 cards

    deck = CardDeck()
    deck.shuffle()
    card = deck.draw()
    """
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()
    
    def _make_deck(self):  # 'private' method
        self._cards = []  # new empty list
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """
        Randomize all cards in deck.
        """
        random.shuffle(self._cards)

    def draw(self):
        """
        Return (and remove) one card from deck. 
        """
        return self._cards.pop()

if __name__ == '__main__':
    d1 = CardDeck()
    print(d1)
    d1.shuffle()
    print(d1.cards)  # not d1.cards()
    for i in range(5):
        card = d1.draw()
        print(card)
