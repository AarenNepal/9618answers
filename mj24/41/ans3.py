#declaring variables to be global
global QueueData
global QueueHead
global QueueTail
QueueData = [] #queue of space 20 elements of type STRING

#initialising the queue
for i in range(20):
    QueueData.append("")

#intialising the pointers
QueueHead = -1
QueueTail = -1

def Enqueue(data):
    global QueueTail
    global QueueHead
    global QueueData
    if QueueTail == 19: #checking to see if queue is full
        return False
    else:
        #if not full
        QueueTail += 1 #increasing tail pointer
        QueueData[QueueTail] = data
        if QueueHead == -1:
            QueueHead += 1 #if first addition to queue increase head pointer
        return True

def Dequeue():
    global QueueHead
    global QueueData
    if QueueHead < 0 or QueueHead == QueueTail or QueueHead > 20: #checking if queue is empty
        return False
    else:
        temp = QueueHead #to refer to later
        QueueHead += 1
        return QueueData[temp]

def StoreItems():
    count = 0
    for _ in range(10): #using _ instead of variable because it isnt referenced in code later
       toCheck =  input("Enter String: ")
       #total of the input
       sumOfInput = int(toCheck[0]) + int(toCheck[1]) * 3 + int(toCheck[2]) + int(toCheck[3]) * 3 + int(toCheck[4]) + int(toCheck[5]) * 3
      # int() changes the value to the closest integer
       divisionOfInput = int(sumOfInput / 10)
       #checking if the number is valid
       if (divisionOfInput == 10 and toCheck[6] == "X") or (divisionOfInput == int(toCheck[6])):
           dataQueue = Enqueue(toCheck[0:6])
          # if dataQueue returns True
           if dataQueue:
               print(f"inserted {toCheck[0:6]}")
           else:
               print("Queue Full")
       else:
           count += 1 #increasing number of invalid items
    print(f"{count} invalid items in input")

StoreItems()
dequeue = Dequeue()
if not dequeue: #if queue is empty
    print("queue empty")
else: #else
    print(dequeue)