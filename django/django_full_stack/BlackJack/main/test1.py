# from main.blackJackGame import Tools
#
# tool = Tools.Tools("huang")
# tool.a()
# from . import b
from main.blackJackGame import Player
from main.blackJackGame import deck
from main.blackJackGame import Card
from main.blackJackGame import Game
# myCard = Card.Card('Ace','Hearts')
# print(myCard)

# mydeck = deck.DeckOfCards()
#
# mydeck.shuffle()
#
# #print(mydeck)
#
# print('*' * 10)
#
# for card in mydeck._deck:
#     print(card,card._value)
#
# print('*' * 50)
#
# print("current card is == ", mydeck.current_card)
#
#
#
# player1 = Player.Player("Tom")
#
# print("deal a card ",mydeck.deal_card())
# player1.getOneCard(mydeck.deal_card())
# player1.info()
# player1.getOneCard(mydeck.deal_card())
# player1.info()
# player1.getOneCard(mydeck.deal_card())
# player1.info()
# player1.getOneCard(mydeck.deal_card())
# player1.info()
# player1.getOneCard(mydeck.deal_card())
# player1.info()
player1 = Player.Player("huang")
player2 = Player.Player("Marry")
round1 =Game.Game(player1,player2)
round1.startGame()
player1.getOneCard(round1.deck.deal_card())
player1.info()
player2.getOneCard(round1.deck.deal_card())
player2.info()