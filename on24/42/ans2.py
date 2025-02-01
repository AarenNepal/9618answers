
class Queue:
    #self.QueueArray: 100 INTEGER values
    #self.HeadPointer: INTEGER
    #self.TailPointer: INTEGER

    def __init__(self, vQueueArray, vHeadPointer, vTailPointer):
        self.QueueArray = vQueueArray
        self.Headpointer = vHeadPointer
        self.Tailpointer= vTailPointer

NewArray = []
for i in range(100):
    NewArray.append(-1)

TheQueue = Queue(NewArray, -1, 0)

def Enqueue(AQueue, TheData):
    if AQueue.Headpointer == -1:
        AQueue.Headpointer = 0
        AQueue.QueueArray[AQueue.Tailpointer] = TheData
        AQueue.Tailpointer +=1
        return 1
    elif AQueue.Tailpointer > 99:
        return -1
    else:
        AQueue.QueueArray[AQueue.Tailpointer] = TheData
        AQueue.Tailpointer += 1
        return 1
def ReturnAllData():
    concat =""
    for i in range(TheQueue.Headpointer, TheQueue.Tailpointer):
        concat = concat + str(TheQueue.QueueArray[i]) + " "
    return concat

def Dequeue():
    if TheQueue.Headpointer == -1:
        return -1
    else:
        temp = TheQueue.QueueArray[TheQueue.Headpointer]
        TheQueue.Headpointer += 1
        return temp


count = 0
while count < 10:
    num = int(input("Enter number: "))
    if num >= 0:
        if Enqueue(TheQueue, num) == -1:
            print("Queue is full")
        else:
            print("Item added to queue ")
        count += 1

print(ReturnAllData())
val = Dequeue()
val2 = Dequeue()
if val == -1:
    print("queue empty")
else:
    print(f"{val} returned")

if val2 == -1:
    print("queue empty")
else:
    print(f"{val2} returned")

print(ReturnAllData())