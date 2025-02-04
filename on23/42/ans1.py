from email.header import Header

StackVowel = [] #1D global array
StackConsonant = [] #1D global array

VowelTop = 0 #pointer for StackVowel
ConsonantTop = 0 #pointer for StackConsonant

def PushData(letter):
    global VowelTop
    global ConsonantTop
    char= letter.lower()
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        StackVowel.append(letter)
        VowelTop +=1
    else:
        StackConsonant.append(letter)
        ConsonantTop +=1

def ReadData():
    file = open("StackData.txt", 'r')
    try:
        for each in file:
            char = each.strip()
            PushData(char)
    except IOError:
        print("file not found")

def PopVowel():
    global VowelTop
    global StackVowel

    if VowelTop == 0:
        return "No data"
    VowelTop -= 1
    ToReturn = StackVowel[VowelTop]
    del StackVowel[-1]
    return ToReturn



def PopConsonant():
    global ConsonantTop
    global StackConsonant

    if ConsonantTop == 0:
        return "No data"

    ConsonantTop -= 1
    ToReturn = StackConsonant[ConsonantTop]
    del StackConsonant[-1]
    return ToReturn


ReadData()

count = 0
Toprint = ""

while True:
    if count == 5:
        break

    choice = input("vowel or consonant")
    if choice.lower() == "vowel":
        value = PopVowel()
        if value == "No data":
            print("Empty Stack")

        Toprint = Toprint + value
        count += 1

    elif choice.lower() == "consonant":
        value = PopConsonant()
        if value == "No data":
            print("Empty Stack")

        Toprint = Toprint + value
        count += 1

print(Toprint)

