import random


ArrayData= [[0]*10 for i in range(10)] #of type integer
for x in range(0, 10):
    for y in range(0,10):
        ArrayData[x][y] = random.randint(1, 100)

def Printarray():
    for x in range(0, 10):
        for y in range(0, 10):
            print(ArrayData[x][y], " ", end='')
        print("")

ArrayLength = 10

def sort():
    for x in range(ArrayLength):
        for y in range(ArrayLength-1):
            for z in range(ArrayLength-y-1):
                if ArrayData[x][z] > ArrayData[x][z+1]:
                    TempValue = ArrayData[x][z]
                    ArrayData[x][z] = ArrayData[x][z+1]
                    ArrayData[x][z+1] = TempValue

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower + Upper ) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    return -1

print("before")
Printarray()
sort()
print("after")
Printarray()
print(BinarySearch(ArrayData, 0, len(ArrayData), 13))
print(BinarySearch(ArrayData, 0, len(ArrayData), 12))