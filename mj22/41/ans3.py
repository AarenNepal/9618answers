from queue import Queue

QueueArray = [None] * 10
HeadPointer = 0
TailPointer = 0
NoOfItems = 0

def Enqueue(DataToAdd):
    global QueueArray
    global HeadPointer
    global TailPointer
    global NoOfItems

    if NoOfItems == 10:
        return "queue full"

    QueueArray[TailPointer] = DataToAdd

    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer +=1

    NoOfItems += 1
    return "added"

def Dequeue():
    global QueueArray
    global HeadPointer
    global TailPointer

    if NoOfItems == 0:
       return False
    else:
        temp = QueueArray[HeadPointer]
        HeadPointer += 1
        return temp

for i in range(11):
    string = input("enter string value")
    print(Enqueue(string))

print(Dequeue())
print(Dequeue())
