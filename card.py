class Card:
    def __init__(self, rank, suit):  #  "dunder init" method
        self.rank = rank
        self.suit = suit

    # human-friendly
    def __str__(self):  # str(obj)
        return f"Card:{self.rank}/{self.suit}"
    
    # code-friendly
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == '__main__':
    c1 = Card('8', 'Diamonds')
    print(c1)
    print(c1.rank)
    c2 = Card('A', 'Spades')
    print(c2)
    print(c2.rank)
