

student_details = {"name": None,"age":None,"percentage":None}
def StudentMarksReport():
    Studentname = input("enter student name: ")
    try:
        Age = int(input("enter your age: "))
        Numberofsubjects = int(input("enter number of subjects: "))
        if Numberofsubjects == 0:
            print("number of subject cant be zero")
            return
    except ValueError:
        print("error kindlly enter a valid value")
        return

    Marksforeachsubject = []
    try:
        for i in range(Numberofsubjects):
            marks = float(input(f"enter marks of subject{i+1}: "))
            Marksforeachsubject.append(marks)
    except ValueError:
        print("error value")
        return
    totalmarks = sum(Marksforeachsubject)
    percentage = (totalmarks / Numberofsubjects) * 100
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage < 60:
        grade = "C"
    student_details["name"] = Studentname
    student_details["age"] = Age
    student_details["percentage"] = percentage
    print(f"grade:{grade}")

def ViewStudentInformationDaysoftheWeek():
    print(student_details["name"])
    print(student_details["age"])
    print(student_details["percentage"])
    days_of_week = ["mon","tue","wed","thu","fri","sat","sun"]
    print(days_of_week[0])
    print(days_of_week[4])
    print(days_of_week[-1])
    print(len(days_of_week))
    try:
        Index = int(input("enter a index to access a day: "))
        print(days_of_week[Index])
    except (ValueError,IndexError):
        print("invalid index")

fruits = ["apple","mango"]
def viewfruits():
    print(fruits)
def addfruits():
    fruits.append("banana")
def insertfruits():
    fruits.insert(0,"orange")
def removefruits():
    fruits.remove("apple")
def addmultiplefruits():
    fruits.extend(["papaya","kiwi"])
def repeatfruits():
    try:
        n = int(input("enter n to repeat list: "))
        print(n*fruits)
    except ValueError:
        print("error value")
def ListOperationsonNumbers():
    List = [1,2,3,4,5]
    print(list(reversed(List)))
    print(list(sorted(List)))
    print(list(sorted(List,reverse=True)))
    print(List.count(1))
    print(1 in List)
def ExtraNumberAnalysis():
    n = input("enter a comma sepreated values: ").split(",")
    num = []
    for i in n:
        try:
            a = float(i)
            num.append(a)
        except ValueError:
            print(f"non numeric value is:{i}")
    if num:
        print(f"minimum value is:{min(num)}")
        print(f"maximum value is:{max(num)}")
        print(f"sum of:{sum(num)}")
        print(f"average of:{sum(num) / len(num)}")
        print(f"valid number is:{len(num)}")
    else:
        print("no valid value")
def NestedListDemonstration():
    a = ["mon",["tue","wed"],"fri","sat","sun"]
    print(len(a))
    try:
        Index = int(input("enter index: "))
        print(a[Index])
        return
    except ValueError:
        print("error value")
    print(a[1][1])
def main():
    while True:
        try:
            Choice = int(input("enter Choice from 1 to 12: "))
        except ValueError:
            print("error value")
            return
        if Choice == 1:
            StudentMarksReport()
        elif Choice == 2:
            ViewStudentInformationDaysoftheWeek()
        elif Choice == 3:
            viewfruits()
        elif Choice == 4:
            addfruits()
        elif Choice == 5:
            insertfruits()
        elif Choice == 6:
            removefruits()
        elif Choice == 7:
            addmultiplefruits()
        elif Choice == 8:
            repeatfruits()
        elif Choice == 9:
            ListOperationsonNumbers()
        elif Choice == 10:
            ExtraNumberAnalysis()
        elif Choice == 11:
            NestedListDemonstration()
        elif Choice == 12:
            print("exit")
            break

main()








