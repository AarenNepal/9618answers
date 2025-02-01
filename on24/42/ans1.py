class EventItem:
    #self.__EventName: STRING
    #self.__Type: STRING
    #Difficulty: INTEGER

    def __init__(self, vEventName, vType, vDifficulty):
        self.__EventName = vEventName
        self.__Type = vType
        self.__Difficulty = vDifficulty

    def GetName(self):
        return self.__EventName

    def GetDifficulty(self):
        return self.__Difficulty

    def GetEventType(self):
        return self.__Type

class Character:
    #self.__CharacterName: STRING
    #self.__Jump: INTEGER
    #self.__Swim: INTEGER
    #self.__Run: INTEGER
    #self.__Drive: INTEGER

    def __init__(self, vChracterName, vJump, vSwim, vRun, vDrive):
        self.__CharacterName = vChracterName
        self.__Jump = vJump
        self.__Swim = vSwim
        self.__Run = vRun
        self.__Drive = vDrive

    def GetName(self):
        return self.__CharacterName

    def CalculateScore(self, Type, difficulty):
        chance = 0
        if Type.upper() == "JUMP":
            chance = self.__Jump
        elif Type.upper() == "SWIM":
            chance = self.__Swim
        elif Type.upper() == "RUN":
            chance = self.__Run
        elif Type.upper() == "DRIVE":
            chance = self.__Drive

        stance = difficulty - chance
        if chance >= difficulty:
            return 100
        elif stance == 1:
            return 80
        elif stance ==2:
            return 60
        elif stance == 3:
            return 40
        elif stance == 4:
            return 20



Group = [EventItem("Bridge", "jump", 3),
         EventItem("Water Wade", "swim", 4),
         EventItem("100 mile run", "run", 5),
         EventItem("Gridlock", "drive", 2),
         EventItem("Wall on wall", "jump", 4)
         ]

Tarz = Character("Tarz", 5, 3, 5, 1)
Geni = Character("Geni", 2, 2, 3, 4)

ScoreTarz = 0
ScoreGeni = 0

for each in Group:
    TarzScore = Tarz.CalculateScore(each.GetEventType(), each.GetDifficulty())
    GeniScore = Geni.CalculateScore(each.GetEventType(), each.GetDifficulty())
    if TarzScore == GeniScore:
        print(f"Draw in {each.GetName()}")
    elif TarzScore > GeniScore:
        print(f"Tarz won {each.GetName()}")
        ScoreTarz += 1
    else:
        print(f"Gein won {each.GetName()}")
        ScoreGeni += 1

if ScoreGeni == ScoreTarz:
    print("Group was draw")
elif ScoreGeni > ScoreTarz:
    print("Geni won the group")
else:
    print("Tarz won the group")