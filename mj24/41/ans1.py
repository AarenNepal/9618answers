global DataStored
global NumberItems
DataStored = [] #array of type integer with space of 20

def Initialise():
    global DataStored
    global NumberItems
    quantity = int(input("Enter the quantity : "))
    if 1 <= quantity <= 20:
        for i in range(quantity):
            num = int(input("Enter number: "))
            DataStored.append(num)
            NumberItems += 1

def BubbleSort():
    global DataStored
    for i in range(len(DataStored) -1):
        for j in range(len(DataStored)-i-1):
            if DataStored[j] > DataStored[j+1]:
                temp = DataStored[j]
                DataStored[j] = DataStored[j+1]
                DataStored[j+1] = temp

def BinarySearch(DataToFind):
    global DataStored
    global NumberItems
    low = 0
    high = NumberItems -1
    while low <= high:
        mid = int((low+high)/2)

        if DataToFind == DataStored[mid]:
            return mid
        elif DataToFind < DataStored[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

NumberItems = 0
Initialise()
BubbleSort()
print(DataStored)

toSearch = int(input("Enter value to search: "))
loc = BinarySearch(toSearch)
if loc == -1:
    print("not found")
else:
    print(f"{toSearch} found at {loc}")

