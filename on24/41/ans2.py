class Horse:
    #self.__Name: STRING
    #self.__MaxFenceHeight: INTEGER
    #self.__PercentageSuccess: INTEGER
    def __init__(self, vName, vMaxFenceHeight, vPercentageSuccess):
        self.__Name = vName
        self.__MaxFenceHeight = vMaxFenceHeight
        self.__PercentageSuccess = vPercentageSuccess

    def GetName(self):
        return self.__Name

    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight

class Fence:
    #self.__Height: INTEGER
    #self.__Risk: INTEGER

    def __init__(self, vHeight, vRisk):
        self.__Height = vHeight
        self.__Risk = vRisk

    def GetHeight(self):
        return self.__Height

    def GetRisk(self):
        return self.__Risk

Horses = [] #1D array of TYPE Horse that stores 2 objects
Course = [] #1D array of TYPE Fence that stores 4 objects

Horses.append(Horse("Beauty", 150, 72))
Horses.append(Horse("Jet", 160, 65))

for each in Horses:
    print(f"{each.GetName()}")

Count = 0
while Count < 4:
    vHeight = int(input("Enter height "))
    vRisk = int(input("Enter risk "))
    if 1 <= vRisk <= 5:
        Fence(vHeight, vRisk)
        Course.append(Fence)
        Count += 1
