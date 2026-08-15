# deck of cards

"""
1. Card Domain Entity:
   - Implement a Card class representing a standard playing card defined by a suit and a value.
   - Restrict instantiation to valid standard card suits ("Hearts", "Diamonds", "Clubs", "Spades") 
     and values ("2" through "10", "J", "Q", "K", "A"). Reject invalid parameters by throwing a ValueError.
   - Provide a formal string representation displaying the card as '{value} of {suit}'.

2. Deck Manager Class:
   - Implement a Deck class that initializes a complete collection of 52 unique Card instances upon creation.
   - Support container size evaluation and custom string representations reflecting remaining card counts.
   - Provide dealing mechanics to draw single cards or multi-card hands from the deck, ensuring 
     graceful handling when draw requests exceed available inventory or when the deck is exhausted.
   - Implement shuffling functionality restricted strictly to full, un-dealt decks.
"""

import random


class Card:

    ALLOWED_SUITS = ("Spade", "Heart", "Diamond", "Club")
    ALLOWED_VALUE = ('A', '2', '3', '4', '5', '6', '7',
                     '8', '9', '10', 'K', 'Q', 'J')

    def __init__(self, suit: str, value: str):
        if suit in Card.ALLOWED_SUITS and value in Card.ALLOWED_VALUE:
            self.suit = suit
            self.value = value
        else:
            raise ValueError("Invalid Suite/Value")

    def __repr__(self):
        return (f"{self.value} of {self.suit}s")


class Deck:

    def __init__(self):
        self.cards = []
        for suit in Card.ALLOWED_SUITS:
            for value in Card.ALLOWED_VALUE:
                self.cards.append(Card(suit, value))

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return (f"{self.count()} left in this Deck.")

    def shuffle(self):
        if self.count() == 52:
            random.shuffle(self.cards)
        else:
            raise ValueError("Deck should be full in order to shuffle")

    def _deal(self, to_dealt):
        curr_count = self.count()
        if curr_count == 0:
            raise ValueError("All cards are dealt")
        else:
            min_cards = min(to_dealt, curr_count)
            dealt_cards = self.cards[-min_cards:]
            self.cards = self.cards[:-min_cards]
            return dealt_cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num: int) -> list[Card]:
        return self._deal(num)
