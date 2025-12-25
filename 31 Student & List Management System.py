student_detail = {"name":None,"age":None,"percentage":None}
def studentmarksreport():
    name = input("enter student name: ")
    while True:
        try:
            age = int(input("enter age: "))
            break
        except ValueError:
            print("value error")
    while True:
        try:
            numberofsubjects = int(input("enter number of subjects: "))
            break
        except ValueError:
            print("value error")
    marks = []
    for i in range(numberofsubjects):
        m = float(input(f"enter marks of subject{i+1}"))
        marks.append(m)
    total_marks = sum(marks)
    percentage = (total_marks / (numberofsubjects * 100)) * 100
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    else:
        grade = "C"
    print(f"grade:{grade}")
    student_detail["name"] = name
    student_detail["age"] = age
    student_detail["percentage"] = percentage
def viewstudentInformationDaysoftheWeek():
    print(student_detail["name"])
    print(student_detail["age"])
    print(student_detail["percentage"])
    days_of_week = ["mon","tue","wed","thu","fri","sat","sun"]
    print(f"First day of the week:{days_of_week[0]}")
    print(f"Fifth day:{days_of_week[4]}")
    print(f"Last day:{days_of_week[-1]}")
    print(f"Total number of days:{len(days_of_week)}")
    while True:
        try:
            Index = int(input("enter a index to access a day: "))
            print(days_of_week[Index])
            break
        except (ValueError,IndexError):
            print("value error")
fruits = ["apple","banana"]
def viewfruits():
    print(fruits)
def addfruits():
    f = input("enter a fruit: ")
    fruits.append(f)
def insertfruit():
    f = input("enter a fruit: ")
    fruits.insert(0,f)
def removefruit():
    f = input("enter a fruit to remove: ")
    if f in fruits:
        fruits.remove(f)
    else:
        print("there is no fruit of that name")
def addmultiplefruits():
    f = input("enter fruits space sepreated").split()
    fruits.extend(f)
def repeatfruits():
    while True:
        try:
            n = int(input("enter fruits to repeat: "))
            print(n*fruits)
            break
        except ValueError:
            print("value error")


num = [1, 4, 3, 2, 6, 8, 9, 56, 0, 54]
def NumberOperations():
    print(list(reversed(num)))
    print(list(sorted(num)))
    print(list(sorted(num,reverse=True)))
    print(num.count(1))
    print(1 in num)
def extranumberanalysis():
    numb = input("enter numbers space sepreated: ").split()
    n = []
    while True:
        try:
            if not n:
                print("no valid number")
            for i in numb:
                a = float(i)
                n.append(a)
            print(f"minimum:{min(n)}")
            print(f"maximum:{max(n)}")
            print(f"sum:{sum(n)}")
            print(f"average:{sum(n) / len(n)}")
            print(f"count of valid numbers:{len(n)}")
            break
        except ValueError:
            print(f"value error:{i}")
def nestedlistdemonstration():
    l = [1,2,[1,2,3,[1]],1]
    print(len(l))
    while True:
        try:
            Index = int(input("enter a index to access element: "))
            print(l[Index])
            break
        except (ValueError,IndexError):
            print("index error")
    print(l[2][3])
def tupledemonstration():
    tupl = (1,2,3,4,5)
    l = list(tupl)
    l.append(6)
    l.remove(1)
    t = tuple(l)
    print(f"length:{len(t)}")
    print(f"first and last element:{t[0]},{t[-1]}")
def main():
    while True:
        try:
            choice = int(input("enter a choice: "))
        except ValueError:
            print("value error")
            continue
        if choice == 1:
            studentmarksreport()
        elif choice == 2:
            viewstudentInformationDaysoftheWeek()
        elif choice == 3:
            viewfruits()
        elif choice == 4:
            addfruits()
        elif choice == 5:
            insertfruit()
        elif choice == 6:
            removefruit()
        elif choice == 7:
            addmultiplefruits()
        elif choice == 8:
            repeatfruits()
        elif choice == 9:
            NumberOperations()
        elif choice == 10:
            extranumberanalysis()
        elif choice == 11:
            nestedlistdemonstration()
        elif choice == 12:
            tupledemonstration()
        elif choice == 13:
            print("exit")
            break
main()









