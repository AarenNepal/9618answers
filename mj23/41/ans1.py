DataArray = [] #1D array of type INTEGER
file = open("Data.txt", "r")
for each in file:
    DataArray.append(int(each.strip()))

def PrintArray(intArray):
    for x in range(len(intArray)):
        print(intArray[x], end=" ")
    print()

def LinearSearch(intArray, searchVal):
    count = 0
    for x in range(0, len(intArray)):
        if intArray[x] == searchVal:
            count += 1
    return count

PrintArray(DataArray)
val = 0
while True:
    val = int(input("Enter value in range 0 to 100: "))
    if 0 <= val <= 100:
        break

times = LinearSearch(DataArray, val)
print(f"The number {val} was found {times} times")