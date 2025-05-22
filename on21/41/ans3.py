ArrayNodes = [[0 for x in range(3)] for y in range(20)] #2D array representing binary tree of type INTEGER with space 20
RootPointer = -1  #points first item in binary tree
FreeNode = 0  #points first empty node in tree

def AddNode(ArrayNodes, RootPointer, FreeNode):
    data = int(input("enter data: "))
    if FreeNode < 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = data
        ArrayNodes[FreeNode][2] = -1

        if RootPointer == -1:
            RootPointer = FreeNode
            FreeNode += 1

        else:
            added = False
            current = RootPointer
            while not added:
                if data < ArrayNodes[current][1]:
                    if ArrayNodes[current][0] == -1:
                        ArrayNodes[current][0] = FreeNode
                        added = True
                    else:
                        current = ArrayNodes[current][0]
                else:
                    if ArrayNodes[current][2] == -1:
                        ArrayNodes[current][2] = FreeNode
                        added = True
                    else:
                        current = ArrayNodes[current][2]

            FreeNode = FreeNode + 1
    else:
        print("tree full")
    return ArrayNodes, RootPointer, FreeNode


def PrintAll():
    for Node in ArrayNodes:
        if Node[0] != 0 and Node[1] != 0 and Node[2] !=0:
            print(Node[0], Node[1], Node[2])

for x in range(10):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)
PrintAll()

def InOrder(ArrayNodes, RootNode):
    if ArrayNodes[RootNode][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][0])
    print(str(ArrayNodes[RootNode][1]))
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][2])

InOrder(ArrayNodes, RootPointer)