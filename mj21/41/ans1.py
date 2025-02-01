class node:
    #self.data: INTEGER
    #self.nextNode: INTEGER
    def __init__(self, vData, vnextNode):
        self.data = vData
        self.nextNode = vnextNode

linkedList = [] #1D array of TYPE node
linkedList.append(node(1, 1))
linkedList.append(node(5, 4))
linkedList.append(node(6, 7))
linkedList.append(node(7, -1))
linkedList.append(node(2, 2))
linkedList.append(node(0, 6))
linkedList.append(node(0, 8))
linkedList.append(node(56, 3))
linkedList.append(node(0, 9))
linkedList.append(node(0, -1))

startPointer = 0
emptyList = 5


def outputNodes(array, startPointer):
    if startPointer >= 0:
        print(array[startPointer].data)
        startPointer = array[startPointer].nextNode
        outputNodes(array, startPointer)

def addNode(linkedList, startPointer, emptyList):
    dataToAdd = int(input("Enter data to be added "))

    if emptyList < 0 or emptyList >9:
        return False
    else:
        newNode = node(int(dataToAdd), -1)
        linkedList[emptyList] = (newNode)

        previousPointer = 0
        while(startPointer != -1):
            previousPointer = startPointer
            startPointer = linkedList[startPointer].nextNode
        linkedList[previousPointer].nextNode = emptyList
        emptyList = linkedList[emptyList].nextNode

        return True

outputNodes(linkedList, startPointer)

if addNode(linkedList, startPointer, emptyList):
    print("Data has been added")
else:
    print("no empty spaces available")

outputNodes(linkedList, startPointer)
