ArrayNodes = []
for i in range(20):
    ArrayNodes.append([-1,-1,-1])

FreeNode = 6
RootPointer = 0

ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10, -1]
ArrayNodes[5] = [-1, 58, -1]
ArrayNodes[6] = [-1, -1, -1]

def SearchValue(Root, ValueToFind):
    if Root == -1:
        return -1
    elif ArrayNodes[Root][1] == ValueToFind:
        return Root
    elif ArrayNodes[Root][1] == -1:
        return -1

    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][1], ValueToFind)

def PostOrder(rootNode):
    if rootNode[0] != -1:
        PostOrder(ArrayNodes[rootNode[0]])
    if rootNode[2] != -1:
        PostOrder(ArrayNodes[rootNode[2]])
    print(str(rootNode[1]))

loc = SearchValue(RootPointer, 15)
if loc == -1:
    print("value not found")
else:
    print(f"Search value found at {loc}")

PostOrder(ArrayNodes[RootPointer])