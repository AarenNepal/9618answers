class Picture:
    #self.__Description: STRING
    #self.__Width: INTEGER
    #self.__Height: INTEGER
    #self.__FrameColour: STRING
    def __init__(self, vDescription, vWidth, vHeight, vFrameColour):
        self.__Description = vDescription
        self.__Width = vWidth
        self.__Height = vHeight
        self.__FrameColour = vFrameColour

    def GetDescription(self):
        return self.__Description

    def GetHeight(self):
        return self.__Height

    def GetWidth(self):
        return self.__Width

    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, vDes):
        self.__Description = vDes

PictureArray = [] #array of type picture
def ReadData():
    global PictureArray
    try:
        file = open("Pictures.txt", "r")
        count = 0
        desc = file.readline().strip()
        while desc != "":
            width = int(file.readline().strip())
            height = int(file.readline().strip())
            colour = file.readline().strip()

            PictureArray.append(Picture(desc, width, height, colour))
            desc = file.readline().strip()
            count += 1
        return count
    except IOError:
        print("file not found")

#main
colour = input("enter the colour: ")
maxWidth = int(input("enter the width: "))
maxHeight = int(input("enter the height: "))
ReadData()
options = []
for picture in PictureArray:
    if picture.GetColour() == colour.lower() and picture.GetWidth() <= maxWidth and picture.GetHeight() <= maxHeight:
        options.append(picture)

for option in options:
    print(option.GetDescription())
    print(option.GetWidth())
    print(option.GetHeight())