student_details = {"name":None,"age":None,"percentage":None}
def studentmarksreport():
    name = input("enter student name: ")
    while True:
        try:
            age = int(input("enter student age: "))
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
    try:
        for i in range(numberofsubjects):
            marks.append(float(input(f"enter marks of subject{i+1}")))
    except ValueError:
        print("value error")
    if marks:
        percentage = (sum(marks) / (numberofsubjects*100)) * 100
        if percentage >= 90:
            grade = "A+"
        elif percentage >=75:
            grade = "A"
        elif percentage >=60:
            grade = "B"
        else:
            grade = "C"
        student_details.update({"name":name,"age":age,"percentage":percentage})
    else:
        print("no valid marks")
day_of_week = []

def viewstudentdetails():
    for i in student_details:
        print(i,student_details[i])
    day_of_week.clear()
    day_of_week.extend(["mon","tue","wed","thu","fri","sat","sun"])
    print(f"First day of the week:{day_of_week[0]}")
    print(f"Fifth day of the week:{day_of_week[4]}")
    print(f"last day of the week:{day_of_week[-1]}")
fruits = ["apple"]
def viewfruits():
    print(fruits)
def addfruits():
    f = input("enter a fruit name: ")
    fruits.append(f)
def inserfruits():
    f = input("enter a fruit name: ")
    fruits.insert(0,f)
def removefruits():
    f = input("enter a fruit: ")
    if f in fruits:
        fruits.remove(f)
    else:
        print("no fruit of that name")
def addmultiplefruit():
    fruits.extend(input("enter fruits name: ").split())
def repeatfruits():
    while True:
        try:
            n = int(input("enter number of times you want repeat fruits: "))
            print(n* fruits)
            break
        except ValueError:
            print("value error")
l = [1,2,4,5,7,3]
def numberoperation():
    print(f"reversed list:{list(reversed(l))}")
    print(f"Sort the list in ascending:{list(sorted(l))}")
    print(f"sort list in descending order:{list(sorted(l,reverse=True))}")
    print(f"Count occurrences of {1} number:{l.count(1)}")
    print(f"Check whether a number exists in the list:{1 in l}")

def extranumberanalysis():
    number = input("enter space sepreated number: ").split()
    n = []
    for i in number:
        try:
            n.append(float(i))
        except ValueError:
            print(f"value error:{i}")
    if n:
        print(f"minimum value is:{min(n)}")
        print(f"maximum value is:{max(n)}")
        print(f"sum:{sum(n)}")
        print(f"average:{sum(n) / len(n)}")
def tupledemonstration():
    try:
        s = "hello world"
        s.replace("a","h")
        s[0] = "a"
    except:
        print("error")
    try:
        t = (1,3,4)
        t[0] = 2
    except:
        print("error")
    l = [1,2]
    l[0] = 0
def main():
    while True:
        try:
            choice = int(input("enter choice from 1 to 13: "))
        except ValueError:
            print("value error")
            continue
        if choice == 1:
            studentmarksreport()
        elif choice == 2:
            viewstudentdetails()
        elif choice == 3:
            viewfruits()
        elif choice == 4:
            addfruits()
        elif choice == 5:
            inserfruits()
        elif choice == 6:
            removefruits()
        elif choice == 7:
            addmultiplefruit()
        elif choice == 8:
            repeatfruits()
        elif choice == 9:
            numberoperation()
        elif choice == 10:
            extranumberanalysis()
        elif choice == 11:
            tupledemonstration()
        elif choice == 12:
            print("break")
            break
main()









