file = open("HighScore.txt", "r")
PlayerArray = [] #2d array of 11 elements

def ReadHighScores():
    for i in range(10):
        Player = file.readline().strip()
        Score = file.readline().strip()

        PlayerArray.append([Player, Score])


def OutputHighScore():
    for each in PlayerArray:
        print(f"{each[0]} {each[1]}")

ReadHighScores()
OutputHighScore()
newPlayer = input("INPUT player name: ")
score = int(input("Enter score: "))

if len(newPlayer) == 3 and 1 <= score <= 100000:
    ...