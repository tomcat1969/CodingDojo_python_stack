import random
from .Card import Card


class DeckOfCards:
    NUMBER_OF_CARDS = 52  # constant number of Cards

    def __init__(self):
        """Initialize the deck."""
        self.current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            newCard = Card(Card.FACES[count % 13],
                            Card.SUITS[count // 13])
            newCard.getCardValue()
            self._deck.append(newCard)

    def shuffle(self):
        """Shuffle deck."""
        self.current_card = 0
        random.shuffle(self._deck)

    def deal_card(self):
        """Return one Card."""
        try:
            card = self._deck[self.current_card]
            self.current_card += 1
            return card
        except:
            return None

    def __str__(self):
        """Return a string representation of the current _deck."""
        s = ''

        for index, card in enumerate(self._deck):
            s += f'{self.deal_card():<19}'
            if (index + 1) % 4 == 0:
                s += '\n'

        return s