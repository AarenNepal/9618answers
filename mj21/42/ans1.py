from numpy.matlib import empty


class node:
    #self.data : INTEGER
    #self.nextnode: INTEGER

    def __init__(self, vdata, vNextNode):
        self.data = vdata
        self.nextNode = vNextNode

LinkedList = [node(1,1),
              node (5, 4),
              node(6,7),
              node(7,-1),
              node(2,2),
              node(0, 6),
              node(0,8),
              node(56,3),
              node(0,9),
              node(0, -1)
              ]
emptyList = 5
startPointer = 0
def outputNodes(array, startPointer):
   if startPointer < 0:
       return -1
   else:
       print(array[startPointer].data)
       if array[startPointer].nextNode != -1:
           outputNodes(array, array[startPointer].nextNode)


def addNode(list, currentPointer, emptyList):
    data = int(input("enter data: "))
    if emptyList < 0 or emptyList > 9:
        return False
    else:
      newNode = node(data, -1)
      list[emptyList] = newNode
      previousPointer = 0
      while (currentPointer != -1):
          previousPointer = currentPointer
          currentPointer = list[currentPointer].nextNode

      list[previousPointer].nextNode = emptyList
      emptyList = list[emptyList].nextNode
      return True

outputNodes(LinkedList, startPointer)
returnVal = addNode(LinkedList, startPointer, emptyList)
if returnVal:
    print("value added")
else:
    print("couldn't add value")
outputNodes(LinkedList, startPointer)
