Queue = [] #global 1D array of type STRING
HeadPointer = -1
TailPointer = 0

def Enqueue(String):
    global Queue
    global HeadPointer
    global TailPointer

    if TailPointer == 50:
        print("the queue is full")
    else:
        Queue.append(String)
        TailPointer +=1
        if HeadPointer == -1:
            HeadPointer = 0

def Dequeue():

    global Queue
    global HeadPointer
    global TailPointer

    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("The queue is empty")
        return "Empty"
    else:
        temp = Queue[HeadPointer]
        HeadPointer +=1
        return temp

def ReadData():
    global Queue
    file = open('QueueData.txt', 'r')
    try:
        for each in file:
            Enqueue(each.strip())
        file.close()
    except IOError:
        print("File not found")

Records = [] #of TYPE RecordData
NumberRecords = 0 #stores number of records in array

class RecordData:
    #self.__ID: STRING
    #self.__Total: INTEGER
    def __init__(self, vID, vTotal):
        self.__ID = vID
        self.__Total = vTotal

    def GetID(self):
        return self.__ID

    def GetTotal(self):
        return self.__Total

    def SetTotal(self, tTotal):
        self.__Total = tTotal

    def SetID(self, tID):
        self.__ID = tID

def TotalData():
    global Records
    global NumberRecords

    DataAccessed = Dequeue()
    Flag = False

    if NumberRecords == 0:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords +=1
        Flag = True
    else:
        for X in range(NumberRecords):
            if Records[X].GetID() == DataAccessed:
                Records[X].SetTotal(Records[X].GetTotal() + 1)
                Flag = True

    if Flag == False:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords +=1

def OutputRecords():
    global Records

    for each in Records:
        print(f"ID {each.GetID()} Total {each.GetTotal()}")

ReadData()
while HeadPointer != TailPointer:
    TotalData()
OutputRecords()