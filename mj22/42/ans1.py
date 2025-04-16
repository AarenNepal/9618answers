global StackData
global StackPointer
StackData = [0]*10
StackPointer = 0

def PrintArray():
    global StackData
    global StackPointer
    print(f"Pointer {StackPointer}")
    for each in StackData:
        print(each)


def Push(integer):
    global StackData
    global StackPointer
    if StackPointer >= 10:
        return False

    StackData[StackPointer] = integer
    StackPointer += 1
    return True

def Pop():
    global StackData
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        temp = StackData[StackPointer-1]
        StackPointer = StackPointer - 1
        del StackData[-1]
        return temp

for i in range(11):
    num = int(input("Enter number: "))
    if Push(num):
        print("Added")
    else:
        print("Stack full")

PrintArray()
Pop()
Pop()
PrintArray()