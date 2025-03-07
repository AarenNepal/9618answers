NumberArray = [100, 85, 644, 22, 15, 8, 1]
NumberArray2 = [100, 85, 644, 22, 15, 8, 1]
def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements -1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False

    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem -= 1
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

def IterativeInsertion(dataArray):
    for i in range(1, len(dataArray)):
        key = dataArray[i]
        j = i - 1
        while j >= 0 and key < dataArray[j]:
            dataArray[j + 1] = dataArray[j]
            j -= 1
        dataArray[j+1] = key
    return dataArray

def BinarySearch(IntegerArray, First, Last, ToFind):
    mid = (First + Last) / 2
    if First > Last:
        return False
    else:
        mid = int((First + Last) / 2)
        if ToFind ==  IntegerArray[mid]:
            return mid
        elif ToFind > IntegerArray[mid]:
           return BinarySearch(IntegerArray, mid+1, Last, ToFind)
        else:
           return BinarySearch(IntegerArray, First, mid-1, ToFind)


toPrint = RecursiveInsertion(NumberArray, len(NumberArray))
print("Recursive")
print(toPrint)
toPrint = IterativeInsertion(NumberArray2)
print("iterative")
print(toPrint)
found = BinarySearch(toPrint, 0, 6, 644)
if not found:
    print("not found")
else:
    print(f"found at {found}")