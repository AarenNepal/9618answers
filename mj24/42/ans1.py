global WordArray
global NumberWords

WordArray = []
NumberWords = 0
def ReadWords(file):
    global WordArray
    global NumberWords
    try:
        fileName = open(file, 'r')
        for each in fileName:
            WordArray.append(each.strip())

        NumberWords = len(WordArray)-1
        fileName.close()
        Play()
    except IOError:
        print("file not found")

def Play():
    print(f"main word: {WordArray[0]} | No of answers = {NumberWords}")
    count = 0
    while True:
        word = input()
        WordArray[0] = ""
        if len(word) < 3:
            print("length should be  > 3")
        if word.lower() == "no":
            break
        elif word.lower() in WordArray:
            count += 1
            print("answer")
            loopCount = 0
            while WordArray[loopCount] != word.lower():
                loopCount += 1

            WordArray[loopCount] = ""
        else:
            print("not answer")


    correctAnswers = (count / NumberWords) * 100
    print(f"answered {correctAnswers}%\n--you missed--")
    for each in WordArray:
        if each != "":
            print(each)

difficulty  = input("Enter the level of difficulty: Easy/Medium/Hard")
difficulty = difficulty.lower()
if difficulty == "easy":
    ReadWords("Easy.txt")
elif difficulty == "medium":
    ReadWords("Medium.txt")
elif difficulty == "hard":
    ReadWords("Hard.txt")


