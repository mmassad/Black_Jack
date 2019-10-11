import random

# This module creates a playing card, with a number, suit and an attribute to determine if it is facing up or down.
# The numbers' values range from 2 to 10; special cards (J, Q, K) are worth 10 and aces are worth 11.
# Suits have a graphic representation and the graphic size of card is also fixed.
# The class Deck creates a list of 52 cards, which can be shuffled. When picking the top card, it is removed from the
# deck.
# Multiple decks can be appended, should the game need more than 52 cards.

class Card:

    def __init__(self, number, suit, hidden):
        self.number = number
        self.suit = suit
        self.hidden = hidden

    list_of_suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    list_of_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    number_to_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                       '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    suits_to_symbol = {'Hearts': '♥', 'Spades': '♠', 'Diamonds': '♦', 'Clubs': '♣'}

    size_of_card = 10

    def check_value(self):
        return Card.number_to_value[self.number]

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(len(Card.list_of_suits)):
            for j in range(len(Card.list_of_numbers)):
                self.cards.append(Card(Card.list_of_numbers[j], Card.list_of_suits[i], True))

    def shuffle(self):
        random.shuffle(self.cards)

    def pick_top(self):
        top = self.cards[0]
        self.cards.pop(0)
        return top

