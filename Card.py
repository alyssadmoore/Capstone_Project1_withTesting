class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "%s of %s" % (self.rank, self.suit)

    def __lt__(self, x):
        y1 = self.rank, self.suit
        y2 = x.rank, x.suit
        return y1 < y2

    def __gt__(self, x):
        y1 = self.rank, self.suit
        y2 = x.rank, x.suit
        return y1 > y2

    def __eq__(self, x):
        y1 = self.rank, self.suit
        y2 = x.rank, x.suit
        return y1 == y2