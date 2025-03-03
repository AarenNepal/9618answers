Jobs = [] #array of integer
NumberOfJobs = 0 #stores number of jobs in array

def Initialise():
    global Jobs
    global NumberOfJobs
    for i in range(100):
        Jobs.append([-1, -1])

    NumberOfJobs = 0

def AddJob(jobNumber, priority):
    global Jobs
    global NumberOfJobs
    if NumberOfJobs == 100:
        print("Not Added")
    else:
        Jobs[NumberOfJobs][0] = jobNumber
        Jobs[NumberOfJobs][1] = priority
        NumberOfJobs +=1
        print("Added")

def InsertionSort():
    global Jobs
    global NumberOfJobs
    for i in range(1, NumberOfJobs):
        Current1 = Jobs[i][0]
        Current2 = Jobs[i][1]
        while i > 0 and Jobs[i - 1][1] > Current2:
            Jobs[i][0] = Jobs[i - 1][0]
            Jobs[i][1] = Jobs[i - 1][1]
            i -= 1
        Jobs[i][0] = Current1
        Jobs[i][1] = Current2

def PrintArray():
    global Jobs
    global NumberOfJobs
    for i  in  range(NumberOfJobs):
        print(f"{Jobs[i][0]} priority {Jobs[i][1]}")

Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)
InsertionSort()
PrintArray()


