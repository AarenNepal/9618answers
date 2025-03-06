global QueueData
global QueueHead
global QueueTail
QueueData = [] #queue of space 20 elements of type STRING
for i in range(20):
    QueueData.append("")

QueueHead = -1
QueueTail = -1

def Enqueue(data):
    global QueueTail
    global QueueHead
    global QueueData
    if QueueTail == 19:
        return False
    else:
        QueueTail += 1
        QueueData[QueueTail] = data
        if QueueHead == -1:
            QueueHead += 1
        return True

def Dequeue():
    global QueueHead
    global QueueData
    if QueueHead < 0 or QueueHead == QueueTail or QueueHead > 20:
        return False
    else:
        temp = QueueHead
        QueueHead += 1
        return QueueData[temp]

def StoreItems():
    count = 0
    for _ in range(10):
       toCheck =  input("Enter String: ")
       sumOfInput = int(toCheck[0]) + int(toCheck[1]) * 3 + int(toCheck[2]) + int(toCheck[3]) * 3 + int(toCheck[4]) + int(toCheck[5]) * 3
       divisionOfInput = int(sumOfInput / 10)
       if (divisionOfInput == 10 and toCheck[6] == "X") or (divisionOfInput == int(toCheck[6])):
           dataQueue = Enqueue(toCheck[0:6])

           if dataQueue:
               print(f"inserted {toCheck[0:6]}")
           else:
               print("Queue Full")
       else:
           count += 1
    print(f"{count} invalid items in input")

StoreItems()
dequeue = Dequeue()
if not dequeue:
    print("queue empty")
else:
    print(dequeue)