import random

class Card():
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def showCard(self):
        print(f'{self.value} of {self.suit}')

    def getValue(self):
        return self.value

class Deck_of_cards():
    def __init__(self):
        self.deck = []
        self.build()

    def build(self):
        for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for value in range(1,14):
                self.deck.append(Card(suit,value))
        
    def showDeck(self):
        for card in self.deck:
            card.showCard()

    def ShuffleDeck(self):
        for card in range(len(self.deck)-1, 0, -1):
            randcard = random.randint(0, card)
            self.deck[card],self.deck[randcard] = self.deck[randcard],self.deck[card]

    def drawCard(self):
        return self.deck.pop()

    def returnCard(self,card):
        self.deck.insert(0,card)

class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self,deck):
        self.hand.append(deck.drawCard())
        
    def getHandValue(self):
        handcount = 0
        for card in self.hand:
            handcount += card.getValue()
        return handcount

    def showHand(self):
        for card in self.hand:
            card.showCard()

    def discardHand(self,deck):
        while len(self.hand) > 0:
            dc = self.hand.pop()
            deck.returnCard(dc)


class Dealer():
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []

    def draw(self,deck):
        self.hand.append(deck.drawCard())

    def getHandValue(self):
        handcount = 0
        for card in self.hand:
            handcount += card.getValue()
        return handcount 

    def showCard(self):
        for card in self.hand:
            card.showCard()
            break

    def showHand(self):
        for card in self.hand:
            card.showCard()

    def discardHand(self,deck):
        while len(self.hand) > 0:
            dc = self.hand.pop()
            deck.returnCard(dc)
    

