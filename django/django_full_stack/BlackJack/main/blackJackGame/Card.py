class Card:

    FACES = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, face, suit):
        """Initialize a Card with a face and suit."""
        self._face = face
        self._suit = suit
        self._value = []


    def getCardValue(self):
        if self._face == 'Ace':
            self._value.append(1)
            self._value.append(11)
            return self._value
        elif self.face == 'Jack' or self.face == 'Queen' or self.face == 'King':
            self._value.append(10)
        elif self.face == '2':
            self._value.append(2)
        elif self.face == '3':
            self._value.append(3)
        elif self.face == '4':
            self._value.append(4)
        elif self.face == '5':
            self._value.append(5)
        elif self.face == '6':
            self._value.append(6)
        elif self.face == '7':
            self._value.append(7)
        elif self.face == '8':
            self._value.append(8)
        elif self.face == '9':
            self._value.append(9)
        elif self.face =='10':
            self._value.append(10)
        # print(self._value)
        return self._value



    @property
    def face(self):
        """Return the Card's self._face value."""
        return self._face

    @property
    def suit(self):
        """Return the Card's self._suit value."""
        return self._suit

    @property
    def image_name(self):
        """Return the Card's image file name."""
        return str(self).replace(' ', '_') + '.png'

    def __repr__(self):
        """Return string representation for repr()."""
        return f"Card(face='{self.face}', suit='{self.suit}')"

    def __str__(self):
        """Return string representation for str()."""
        return f'{self.face} of {self.suit}'

    def __format__(self, format):
        """Return formatted string representation."""
        return f'{str(self):{format}}'