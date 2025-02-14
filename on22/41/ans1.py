DataArray = [] #100 INTEGER

def ReadFile():
    global DataArray
    file = open('IntegerData.txt', 'r')
    try:
        for each in file:
            DataArray.append(int(each.strip()))
    except IOError:
        print("No file found")

def FindValues():
    count = 0
    while True:
        searchValue = int(input("Enter search vaue: "))
        if 1 <= searchValue <= 100:
            break

    for i in range(len(DataArray)):
        if DataArray[i] == searchValue:
            count += 1
    return count

def BubbleSort():
    for i in range(len(DataArray) - 1):
        for j in range(len(DataArray) - i  - 1):
            if DataArray[j] > DataArray[j+1]:
                temp = DataArray[j]
                DataArray[j] = DataArray[j+1]
                DataArray[j+1] = temp
    print(DataArray)


ReadFile()
print(DataArray)
print(f"the search value appeared {FindValues()} times")
BubbleSort()
