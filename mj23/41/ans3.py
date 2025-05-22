
global Animal #1D array of 20 elements
global Colour #1D array of 10 colours
global AnimalTopPointer
global ColourTopPointer
AnimalTopPointer = 0
Animal = [None] * 20
Colour = [None] * 10
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global AnimalTopPointer
    global Animal

    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True

def PopAnimal():
    global AnimalTopPointer
    global Animal

    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -=1
        return ReturnData


def PushColour(DataToPush):
    global ColourTopPointer
    global Colour

    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True


def PopColour():
    global ColourTopPointer
    global Colour

    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData

def ReadData():
    try:
        AnimalFile = open("AnimalData.txt", "r")
        for line in AnimalFile:
            PushAnimal(line.strip())

        AnimalFile.close()
    except IOError:
        print("file not found ")


    try:
        ColourFile =  open("ColourData.txt", "r")
        for line in ColourFile:
            PushColour(line.strip())

        ColourFile.close()
    except IOError:
        print("file not found ")

def OutputItem():
    colour = PopColour()
    animal = PopAnimal()

    if colour == "":
        PushAnimal(animal)
        print("No colour")
    elif animal == "":
        PushColour(colour)
        print("No animal ")
    else:
        print(f"{colour} {animal}")

#main
ReadData()
for i in range(4):
    OutputItem()