import datetime
class Character:
    #self.__CharacterName: STRING
    #self.__DateOfBirth: DATE
    #self.__Intelligence: REAL
    #self.__Speed: INTEGER
    def __init__(self, vCharName, vDateOfBirth, vIntelligence, vSpeed):
        self.__CharacterName = vCharName
        self.__DateOfBirth = vDateOfBirth
        self.__Intelligence = vIntelligence
        self.__Speed = vSpeed

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    def SetIntelligence(self, intel):
        self.__Intelligence = intel

    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1

    def ReturnAge(self):
        return 2025 - self.__DateOfBirth.year

class MagicCharacter(Character, ):
    #self.__Element: STRING
    def __init__(self, vCharName, vDateOfBirth, vIntelligence, vSpeed, vElement):
        super().__init__(vCharName, vDateOfBirth, vIntelligence, vSpeed)
        self.__Element = vElement

    def Learn(self):
        if self.__Element == "fire" or self.__Element == "water":
            self.SetIntelligence(self.GetIntelligence() * 1.2)
        elif self.__Element == "earch":
            self.SetIntelligence(self.GetIntelligence() * 1.3)
        else:
            self.SetIntelligence(self.GetIntelligence() * 1.1)

FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30)
FirstCharacter.Learn()

FirstMagic = MagicCharacter("Light", datetime.datetime(2018, 3, 3), 75, 22, "fire")
FirstMagic.Learn()

print(f"{FirstCharacter.GetName()} is {FirstCharacter.ReturnAge()} years old and has intelligence of {FirstCharacter.GetIntelligence()}")
print(f"{FirstMagic.GetName()} is {FirstMagic.ReturnAge()} years old and he has intelligence of {FirstMagic.GetIntelligence()}")
