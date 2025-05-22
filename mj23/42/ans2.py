global CircularQueue #array of 5 item of type SaleData
global Head
global Tail
global NumberOfItems
CircularQueue = []

class SaleData:
    #self.SaleID: STRING
    #self.SaleQuantity: INTEGER
    def __init__(self, vSaleID, vSaleQuantity):
        self.SaleId = vSaleID
        self.SaleQuantity = vSaleQuantity

def Enqueue(newRecord):
    global CircularQueue
    global Head
    global Tail
    global NumberOfItems
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = newRecord
        if Tail == 4:
            Tail = 0
        else:
            Tail += 1
        NumberOfItems += 1
        return 1

def Dequeue():
    global Head
    global Tail
    global CircularQueue
    global NumberOfItems

    if NumberOfItems == 0:
        return SaleData("", -1)
    else:
        toReturn = CircularQueue[Head]
        if Head == 4:
            Head = 0
        else:
            Head +=1
            NumberOfItems -= 1
        return toReturn

def EnterRecord( ):
    id = input("Enter id: ")
    quantity = input("Enter quantity: ")
    saleRecord = SaleData(id, quantity)
    status = Enqueue(saleRecord)
    if status == -1:
        print("Full")
    elif status == 1:
        print("Stored")

for x in range(5):
    CircularQueue.append(SaleData("", -1))

Head = 0
Tail = 0
NumberOfItems = 0

for x in range(6):
    EnterRecord()

Status = Dequeue()
if Status.SaleId == "":
    print("Queue Empty")
else:
    print(f"{Status.SaleId} {Status.SaleQuantity}")

EnterRecord()

for each in CircularQueue:
    print(f"{each.SaleId} {each.SaleQuantity}")