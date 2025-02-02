HighScores = [['' for _ in range(3)] for y in range(7)]

def ReadData():
    file = open('HighScoreTable.txt', 'r')
    tempArray =[]
    for x in range(7):
        PlayerName = file.readline().strip()
        GameLevel = file.readline().strip()
        Score = file.readline().strip()
        tempArray.append([PlayerName, GameLevel, Score])
    return tempArray

def OutputHighScores(array):
    for each in array:
        toReturn = f"{each[0]} reached level {each[1]} with a score of {each[2]}"
        print(toReturn)

def SortScores():
    for i in range(len(HighScores) -1):
        for j in range(len(HighScores) - i- 1):
            if int(HighScores[j][1]) < int(HighScores[j+1][1]):
                temp1 = HighScores[j][0]
                temp2 = HighScores[j][1]
                temp3 = HighScores[j][2]

                HighScores[j][0] = HighScores[j+1][0]
                HighScores[j][1] = HighScores[j+1][1]
                HighScores[j][2] = HighScores[j+1][2]
                HighScores[j+1][0] = temp1
                HighScores[j+1][1] = temp2
                HighScores[j+1][2] = temp3
    return HighScores

HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
HighScores = SortScores()
print("after")
OutputHighScores(HighScores)
