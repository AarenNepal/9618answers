class Tree:
    #self.__TreeName: STRING
    #self.__HeightGrowth: INTEGER
    #self.__MaxHeight: INTEGER
    #self.__MaxWidth: INTEGER
    #self.__Evergreen: STRING
    def __init__(self, vTreeName, vHeightGrowth, vMaxHeight, vMaxWidth, vEvergreen):
        self.__TreeName = vTreeName
        self.__HeightGrowth = vHeightGrowth
        self.__MaxHeight = vMaxHeight
        self.__MaxWidth = vMaxWidth
        self.__Evergreen = vEvergreen

    def GreenTreeName(self):
        return self.__TreeName

    def GetGrowth(self):
        return self.__HeightGrowth

    def GetMaxHeight(self):
        return self.__MaxHeight

    def GetMaxWidth(self):
        return self.__MaxWidth

    def GetEvergreen(self):
        return self.__Evergreen

def ReadData():
    Array = []
    try:
        file = open("Trees.txt", "r")
        for each in file:
            splitted = each.split(",")
            Array.append(Tree(splitted[0], int(splitted[1]), int(splitted[2]), int(splitted[3]), splitted[4]))
    except IOError:
        print("File not found")
    return Array

def PrintTrees(tree):
    if tree.GetEvergreen().lower() == "yes":
        print(f"{tree.GreenTreeName()} has a maximum height {tree.GetMaxHeight()} a maximum width {tree.GetMaxWidth()} and grows {tree.GetGrowth()}cm a year. It does not lose its leaves.")
    else:
        print(f"{tree.GreenTreeName()} has a maximum height {tree.GetMaxHeight()} a maximum width {tree.GetMaxWidth()} and grows {tree.GetGrowth()}cm a year. It loses its leaves each year.")

def ChooseTree(treeArray):
    maxHeightRequired = int(input("Enter max height: "))
    maxWidthRequired = int(input("Enter max width: "))
    everGreenBool = input("do you want it to be evergreen? (yes/no)")
    options = []
    if everGreenBool.lower() == "yes":
        keep = "yes"
    else:
        keep = "no"

    for tree in treeArray:
        if tree.GetMaxWidth() <= maxWidthRequired and tree.GetMaxHeight() <= maxHeightRequired and tree.GetEvergreen().lower() == keep:
            options.append(tree)

    return options
returnValue = ReadData()
PrintTrees(returnValue[0])
print(ChooseTree(returnValue))
