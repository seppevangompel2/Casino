#info from geeksforgeeks.org
import random

class Card:
    def __init__(self, card, category):
        self.card = card
        self.category = category

    def value(self):
        if self.card in ['Jack', 'Queen', 'King']:
            return 10
        elif self.card == 'Ace':
            return 11
        else:
            return int(self.card)

    def __repr__(self):
        return f"{self.card} of {self.category}"

class Deck:
    card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self):
        self.cards = [Card(card, category) for category in self.card_categories for card in self.cards_list]
        random.shuffle(self.cards)

    def pop(self):
        return self.cards.pop()
