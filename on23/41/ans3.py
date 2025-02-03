class Character:
    #self.__Name: STRING
    #self.__XPosition: INTEGER
    #self.__YPosition: INTEGER

    def __init__(self, vName, vXPosition, vYPosition):
        self.__Name = vName
        self.__XPosition = vXPosition
        self.__YPosition = vYPosition

    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self, tXPosition):
        self.__XPosition = self.__XPosition + tXPosition
        if self.__XPosition > 10000:
            self.__XPosition = 10000
        elif self.__XPosition < 0:
            self.__XPosition = 0

    def SetYPosition(self, tYPosition):
        self.__YPosition = self.__YPosition + tYPosition
        if self.__YPosition > 10000:
            self.__YPosition = 10000
        elif self.__YPosition < 0:
            self.__YPosition = 0

    def Move(self, direction):
        direction = direction.lower()
        if direction == "up":
            self.SetYPosition(10)
        elif direction == "down":
            self.SetYPosition(-10)
        elif direction == "left":
            self.SetXPosition(-10)
        elif direction == "right":
           self.SetXPosition(10)

class BikeCharacter(Character):
    # self.__Name: STRING
    # self.__XPosition: INTEGER
    # self.__YPosition: INTEGER
    def __init__(self, vName, vXPosition, vYPosition):
        super().__init__(vName, vXPosition, vYPosition)

    def Move(self, direction):
        direction = direction.lower()
        if direction == "up":
           super().SetYPosition(20)
        elif direction == "down":
            super().SetYPosition(-20)
        elif direction == "left":
            super().SetXPosition(-20)
        elif direction == "right":
           super().SetXPosition(20)

Jack = Character("Jack", 50, 50)
Karla = BikeCharacter("Karla", 100, 50)

Char = input("Which character do you want to move?: ")
Direction = input("Which direction do you want the character to move?: ")

if Char.lower() == "jack":
    Jack.Move(Direction)
    print(f"{Char}'s new position is X = {Jack.GetXPosition()} and Y = {Jack.GetYPosition()}")
elif Char.lower() == "karla":
    Karla.Move(Direction)
    print(f"{Char}'s new position is X = {Karla.GetXPosition()} and Y = {Karla.GetYPosition()}")





