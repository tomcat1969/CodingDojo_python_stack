from .deck import DeckOfCards
from .Player import Player
from .Card import Card
class Game:
    def __init__(self,player1,player2):
        self.deck = DeckOfCards()
        self.deck.shuffle()
        self.gameOver = False
        self.player1 = player1
        self.player2 = player2

    def startGame(self):
        self.player1.getOneCard(self.deck.deal_card())
        self.player2.getOneCard(self.deck.deal_card())
        self.player1.getOneCard(self.deck.deal_card())
        self.player2.getOneCard(self.deck.deal_card())
        self.player1.info()
        self.player2.info()

    def allPlayersGetOneCard(self):
        self.player1.getOneCard(self.deck.deal_card())
        self.player2.getOneCard(self.deck.deal_card())
        self.player1.info()
        self.player2.info()



