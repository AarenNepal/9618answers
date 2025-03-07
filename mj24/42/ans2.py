class Node:
    def __init__(self, vData):
        self.__LeftPointer = -1
        self.__Data = vData
        self.__RightPointer = -1

    def GetLeft(self):
        return self.__LeftPointer

    def GetRight(self):
        return self.__RightPointer

    def GetData(self):
        return self.__Data

    def SetLeft(self, left):
        self.__LeftPointer = left

    def SetRight(self, right):
        self.__RightPointer = right

    def SetData(self, data):
        self.__Data = data


class TreeClass:
    def __init__(self):
        self._Tree = [Node(-1) for _ in range(20)]
        self._FirstNode = -1
        self._NumberNode = 0  # Fixed variable name

    def InsertNode(self, NewNode):
        if self._FirstNode == -1:
            self._Tree[self._NumberNode] = NewNode
            self._FirstNode = 0
            self._NumberNode += 1  # Fixing the incorrect update
        else:
            self._Tree[self._NumberNode] = NewNode
            NodeAccess = self._FirstNode
            Direction = ""
            Previous = NodeAccess
            while NodeAccess != -1:
                Previous = NodeAccess
                if NewNode.GetData() < self._Tree[NodeAccess].GetData():
                    NodeAccess = self._Tree[NodeAccess].GetLeft()
                    Direction = "left"
                elif NewNode.GetData() > self._Tree[NodeAccess].GetData():
                    NodeAccess = self._Tree[NodeAccess].GetRight()
                    Direction = "right"

            if Direction == "left":
                self._Tree[Previous].SetLeft(self._NumberNode)
            else:
                self._Tree[Previous].SetRight(self._NumberNode)

            self._NumberNode += 1  # Properly update the node count

    def OutputTree(self):
        if self._NumberNode == 0:
            print("No nodes")
        else:
            for x in range(self._NumberNode):
                print(self._Tree[x].GetLeft(), " ", self._Tree[x].GetData(), " ", self._Tree[x].GetRight())

TheTree = TreeClass()

TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))

TheTree.OutputTree()
