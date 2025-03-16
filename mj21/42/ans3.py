class TreasureChest:
    #self.__question: STRING
    #self.__answer: INTEGER
    #self.__points: INTEGER

    def __init__(self, vQuestion, vAnswer, vPoints):
        self.__question =vQuestion
        self.__answer = vAnswer
        self.__points = vPoints

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, ans):
        if ans == int(self.__answer):
            return True

    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points) //2
        elif attempts == 3 or attempts == 4:
            return int(self.__points) // 4
        else:
            return 0
arrayTreasure = []
def readData():
    file = open("TreasureChestData.txt", "r")
    for i in range(5):
       question =  file.readline().strip()
       answer = file.readline().strip()
       points = file.readline().strip()

       arrayTreasure.append(TreasureChest(question, answer, points))

readData()

while True:
    quesNo = int(input("Enter a number between 1 & 5: "))
    if 1 <= quesNo <= 5:
        break


print(f"Question {quesNo}: {arrayTreasure[quesNo-1].getQuestion()}: ")
ans = int(input())

count = 0
while True:
    count = count + 1
    if arrayTreasure[quesNo-1].checkAnswer(ans):
        print("Answer correct")
        break

point= arrayTreasure[quesNo - 1].getPoints(count)
print(f"you have been awarded {point} points")
