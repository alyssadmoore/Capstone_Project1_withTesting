import random, Card


class Deck:
    def __init__(self):
        self.ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        self.deck = []
        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append(Card.Card(rank, suit))

        random.shuffle(self.deck)

    def draw_card(self):
        card = self.deck.pop()
        return card
