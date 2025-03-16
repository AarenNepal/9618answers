global arrayData
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(searchvalue):
    for each in arrayData:
        if searchvalue == int(each):
            return True
        else:
            return False

def bubbleSort():
    global arrayData
    for x in range(len(arrayData)):
        for y in range(len(arrayData) - x - 1):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

search = int(input("enter search value: "))
status = linearSearch(search)
if status:
    print("value found ")
else:
    print("value not found")
bubbleSort()