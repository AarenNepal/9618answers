StringArray =[] #local array of type string for 45 items
#meow
def ReadData():
    try:
        file = open("Data.txt", 'r')
        for each in file:
            StringArray.append(each.strip())
        print(StringArray)
    except FileNotFoundError:
        print("File not found")

def FormatArray(array):
    String = ""
    for each in array:
        String = String + " " + each
    return String

def CompareString(String1, String2):
    count = 0
    while True:
        if String1[count] < String2[count]:
            return 1
        elif String1[count] > String2[count]:
            return 2
        else:
            count += 1

def Bubble(array):
    for i in range(len(array) -1 ):
        for j in range(len(array) - 1 - i):
            if CompareString(array[j], array[j+1]) == 2:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
ReadData()
print(FormatArray(StringArray))
Bubble(StringArray)
print(FormatArray(StringArray))
