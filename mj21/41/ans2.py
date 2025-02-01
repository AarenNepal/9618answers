global arrayData #global 1D array of type INTEGER
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

found = False
def linearSearch(searchVal):
    for i in range(10):
        if arrayData[i] == searchVal:
            found = True
        else:
            found = False
    return found

searchValue = int(input("Enter search value: "))
if linearSearch(searchValue):
    print("Value has been found")
else:
    print("Value not found")

def bubbleSort():
    theArray = arrayData
    for x in range(0, len(theArray)):
        for y in range(0, len(theArray) - x -1 ):
            if theArray[y] < theArray[y+1]:
                temp = theArray[y]
                theArray[y] = theArray[y+1]
                theArray[y+1] = temp
bubbleSort()
print(arrayData)