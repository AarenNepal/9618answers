class Vehicle:
    #self.__ID: STRING
    #self.__MaxSpeed: INTEGER
    #self.__CurrentSpeed: INTEGER
    #self.__IncreaseAmount: INTEGER
    #self.__HorizontalPosition: INTEGER
    def __init__(self, vID, vMaxSpeed, vIncreaseAmount):
        self.__ID = vID
        self.__MaxSpeed = vMaxSpeed
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = vIncreaseAmount
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, vSpeed):
        self.__CurrentSpeed = vSpeed

    def SetHorizontalPosition(self, hPos):
        self.__HorizontalPosition = hPos

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed

    def OutputCurrentPosition(self):
        print("Current position = ", self.__HorizontalPosition)
        print("Current speed = ", self.__CurrentSpeed)

class Helicopter(Vehicle):
    #self.__VerticalPosition: INTEGER
    #self.__VerticalChange: INTEGER
    #self.__MaxHeight: INTEGER
    def __init__(self, vID, vMaxSpeed, vIncreaseAmount, vVerticalChange, vMaxHeight ):
        super().__init__(vID, vMaxSpeed, vIncreaseAmount)
        self.__VerticalPosition = 0
        self.__VerticalChange = vVerticalChange
        self.__MaxHeight = vMaxHeight

    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight

        currentSpeed = self.GetCurrentSpeed() + self.GetIncreaseAmount()
        if currentSpeed > self.GetMaxSpeed():
            currentSpeed = self.GetMaxSpeed()
        self.SetCurrentSpeed(currentSpeed)
        self.SetHorizontalPosition(self.GetHorizontalPosition() + currentSpeed)

    def OutputCurrentPosition(self):
        print("Current position = ", Vehicle.GetHorizontalPosition(self))
        print("Current speed = ", Vehicle.GetCurrentSpeed(self))
        print("Current verticalposition = ", self.__VerticalPosition)

car = Vehicle("Tiger", 100, 20)
helicopter = Helicopter("Lion", 250, 40, 3, 100)
car.IncreaseSpeed()
car.IncreaseSpeed()
car.OutputCurrentPosition()
helicopter.IncreaseSpeed()
helicopter.IncreaseSpeed()
helicopter.OutputCurrentPosition()
