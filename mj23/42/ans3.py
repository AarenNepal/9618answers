class Employee:
    #self.__HourlyPay: REAL
    #self.__EmployeeNumber: STRING
    #self.__JobTitle: STRING
    #self.__PayYear2022: ARRAY[0:51] OF REAL
    def __init__(self, vHourlyPay, vEmployeeNumber, vJobTitle):
        self.__HourlyPay = vHourlyPay
        self.__EmployeeNumber = vEmployeeNumber
        self.__JobTitle = vJobTitle
        self.__PayYear2022 = [0.0]*51

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, week, hours):
        pay = self.__HourlyPay * hours
        self.__PayYear2022[week-1] = pay

    def GetTotalPay(self):
       total = 0
       for x in range(0, 51):
           total = total + self.__PayYear2022[x]
       return total

class Manager(Employee):
    #self.__BonusValue: SINGLE
    def __init__(self, vHourlyPay, vEmployeeNumber, vJobTitle, vBonusValue):
        super().__init__(vHourlyPay, vEmployeeNumber, vJobTitle)
        self.__BonusValue = vBonusValue

    def SetPay(self, week, hours):
        hours = hours *(1+self.__BonusValue / 100)
        super().SetPay(week, hours)

def EnterHours():
    try:
        datafile = open("HoursWeek1.txt", "r")
        for x in range(8):
            dataEmp = datafile.readline().strip()
            hours = float(datafile.readline().strip())
            for y in range(8):
                if EmployeeArray[y].GetEmployeeNumber() == dataEmp:
                    EmployeeArray[y].SetPay(1, hours)
    except IOError:
        print("File not found")
#main
EmployeeArray = [] #1D array with capacity 8 of type EMPLOYEE
file = open("Employees.txt", "r")
Pay = 0.00
id = " "
bonus = 0.00
title = " "
temp = " "
try:
    file = open("Employees.txt", "r")
    for x in range(8):
        Pay = float(file.readline().strip())
        empId = file.readline().strip()
        temp = file.readline().strip()

        try:
            bonus = float(temp)
            title = file.readline().strip()
            EmployeeArray.append(Manager(Pay, empId, title, bonus))
        except:
            title = temp
            EmployeeArray.append(Employee(Pay, empId, title))

    file.close()
except IOError:
    print("file not found")


EnterHours()
for x in range(len(EmployeeArray)):
    print(f"{EmployeeArray[x].GetEmployeeNumber()} : {EmployeeArray[x].GetTotalPay()}")


