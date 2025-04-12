class Balloon:
    #self.__Health: INTEGER
    #self.__Colour: STRING
    #self.__DefenceItem: STRING

    def __init__(self, vColour, vDefenceItem):
        self.__Health = 100
        self.__Colour = vColour
        self.__DefenceItem = vDefenceItem

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, num):
        self.__Health = self.__Health + num

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False

def Defend(balloon):
    strength = int(input("Enter strength of opponent: "))
    balloon.ChangeHealth(-strength)

    print(f"Defence item: {balloon.GetDefenceItem()}")
    if balloon.CheckHealth():
        print("no health remaining")
    else:
        print("defended successfully")

    return balloon
item = input("Enter defence item: ")
colour = input("Enter colour: ")

Balloon1 = Balloon(colour, item)
Defend(Balloon1)