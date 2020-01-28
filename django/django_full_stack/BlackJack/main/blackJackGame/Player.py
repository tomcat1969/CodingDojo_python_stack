from . import Card, deck


class Player:
    def __init__(self,nickName):
        """Initialize the player."""
        self.nickName = nickName
        self.current_card = 0
        self._cardsInHand = []
        self.value = {}
        self.currentValue = 0
        self.isDead = False

    def getOneCard(self,card):
        self._cardsInHand.append(card)
        self.calculateValue()
        self.currentValue = self.currentVal()
        if self.currentValue == 0:
            self.isDead = True

    def calculateValue(self): ## give all possible values
        if self._cardsInHand == None:
            self.value = {}
            return
        temp_list = [0]
        for card in self._cardsInHand:
            if len(card._value) == 1:
                for i in range(0,len(temp_list)):
                    temp_list[i] += card._value[0]

            else:
                l1 = list(temp_list)
                l2 = list(temp_list)
                for i in range(0,len(l1)):
                    l1[i] += card._value[0]
                for i in range(0,len(l2)):
                    l2[i] += card._value[1]
                temp_list = list(l1 + l2)

        self.value = set(temp_list)

    def currentVal(self):
        currentValue = 0
        for val in self.value:
            if val > 21:
                pass
            elif val > currentValue:
                currentValue = val
            else:
                pass
            return currentValue




    def info(self):
        print(f"My name is {self.nickName}, I have {self._cardsInHand} on my hand, the value could be {self.value} but the current val is {self.currentValue} so isDead == {self.isDead}")
