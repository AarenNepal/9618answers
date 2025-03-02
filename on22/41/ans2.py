class Card:
    #self.__Number: INTEGER
    #self.__Colour: STRING

    def __init__(self, vNumber, vColour):
        self.__Number = vNumber
        self.__Colour = vColour

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

class Hand:
    #self.__Cards: ARRAY[0:9] OF Card
    #self.__FirstCard: INTEGER
    #self.__NumberCards: INTEGER

    def __init__(self, vCards, vFirstCard, vNumberCards):
        self.__Cards = vCards
        self.__FirstCard = vFirstCard
        self.__NumberCards = vNumberCards

    def GetCard(self, vIndex):
        return self.__Cards[vIndex]

OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")

OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")

OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")

Player1 = Hand([OneRed, TwoRed, ThreeRed, FourRed, OneYellow], 0, 5)
Player2 = Hand([TwoYellow, ThreeYellow, FourYellow, FiveYellow, OneBlue], 0, 5)

def CalculateValue(hand):
    Score = 0
    for i in range(5):
        CardGot = hand.GetCard(i)
        Score = Score + CardGot.GetNumber()
        Colour = CardGot.GetColour()
        if Colour == "red":
            Score = Score + 5
        elif Colour == "blue":
            Score = Score + 10
        else:
            Score = Score + 15
    return Score

Score1 = CalculateValue(Player1)
Score2 = CalculateValue(Player2)
if Score1 >  Score2:
    print("Player 1 won")
elif Score2 > Score1:
    print("Player 2 won")
else:
    print("Its a draw")

