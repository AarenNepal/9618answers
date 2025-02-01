global LinkedList 
global FirstEmpty
global FirstNode

FirstEmpty = 0
FirstNode = -1

Linkedlist = []

for i in range(20):
    if i == 19:
        Linkedlist.append([-1, -1])
    else: 
        Linkedlist.append([-1, i+1])

def InsertData():
    global LinkedList 
    global FirstNode 
    global FirstEmpty
    for _ in range(5):
        if FirstEmpty != -1:
            nextEmpty = Linkedlist[FirstEmpty][1]
            Linkedlist[FirstEmpty][0] = int(input("value: "))
            Linkedlist[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = nextEmpty 

def OutputLinkedList():
    global Linkedlist
    global FirstNode 
    global FirstEmpty
    CurrentPointer = FirstNode
    while True:
        print(Linkedlist[CurrentPointer][0])
        CurrentPointer = Linkedlist[CurrentPointer][1]
        if CurrentPointer == -1:
            break

def RemoveData(ItemToRemove):
    global Linkedlist
    global FirstNode
    global FirstEmpty

    if Linkedlist[FirstNode][0] == ItemToRemove:
        NewFirst = Linkedlist[FirstNode][1]
        Linkedlist[FirstNode][1] = FirstEmpty
        FirstEmpty = FirstNode
        FirstNode = NewFirst
    elif FirstNode != -1:
        CurrentPointer = FirstNode 
        PreviousNode = -1
        while ItemToRemove != Linkedlist[CurrentPointer][0] and CurrentPointer != -1:
            PreviousNode = CurrentPointer
            CurrentPointer = Linkedlist[CurrentPointer][1] 

        if ItemToRemove == Linkedlist[CurrentPointer][0]:
            Linkedlist[PreviousNode][1] = Linkedlist[CurrentPointer][1]
            Linkedlist[CurrentPointer][0] = -1 
            Linkedlist[CurrentPointer][1] = FirstEmpty
            FirstEmpty = CurrentPointer

InsertData()
OutputLinkedList()
RemoveData(5)
print("After")
OutputLinkedList()