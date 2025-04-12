file = open("HighScore.txt", "r")
PlayerArray = [] #2d array of 11 elements

def ReadHighScores():
    for i in range(10):
        Player = file.readline().strip()
        Score = file.readline().strip()

        PlayerArray.append([Player, Score])

    file.close()


def OutputHighScore():
    for each in PlayerArray:
        print(f"{each[0]} {each[1]}")


def NewList(player, score):
    for x in range(0, 10):
        if score > int(PlayerArray[x][1]):
            Temp1 = PlayerArray[x][0]
            Temp2 = PlayerArray[x][1]

            PlayerArray[x][0] = player
            PlayerArray[x][1] = score

            count  = x + 1

            while count < 10:
                sec1 = PlayerArray[count][0]
                sec2 = PlayerArray[count][1]

                PlayerArray[count][0] = Temp1
                PlayerArray[count][1] = Temp2

                Temp1 = sec1
                Temp2 = sec2

                count +=1
            break

def WriteTopTen():
    newFile = open("NewHighScore.txt", "w")
    for each in PlayerArray:
        newFile.write(f"{str(each[0])}\n")
        newFile.write(f"{str(each[1])}\n")

ReadHighScores()
OutputHighScore()
newPlayer = input("INPUT player name: ")
score = int(input("Enter score: "))
if len(newPlayer) == 3 and 1 <= score <= 100000:
    NewList(newPlayer, score)

OutputHighScore()
WriteTopTen()