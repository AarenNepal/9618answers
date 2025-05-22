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

global chosenArray
chosenArray = []
for _ in range(30):
    chosenArray.append(1)

def ChooseCard():
    global chosenArray
    while True:
        index = int(input("Enter a number from 1 to 30: "))
        if 1 <= index <= 30:
            if chosenArray[index-1] == 1:
                chosenArray[index-1] = 0
                print("valid")
                return index -1
            else:
                print("Card chosen")
        else:
            print("invalid range ")

CardArray = [] #array with 30 elements
file = open("CardValues.txt", "r")
for i in range(30):
    num = file.readline().strip()
    colour = file.readline().strip()

    CardArray.append(Card(num, colour))

Player1 = [] #array of type Card for player 1
for i in range(4):
    Player1.append(CardArray[ChooseCard()])

for x in range(len(Player1)):
    print(f"{Player1[x].GetNumber()} {Player1[x].GetColour()}")



