student_details = {"name":None,"age":None,"percentage":None}
def studentmarksreport():
    studentname = input("enter student name: ")
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
    for i in range(numberofsubjects):
        marks.append(float(input(f"enter marks of subject{i+1}")))
    percentage = (sum(marks) / (numberofsubjects*100)) * 100
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage < 60:
        grade = "C"
    print(f"grade:{grade}")
    student_details.update({"name":studentname,"age":age,"percentage":percentage})
day_of_week = ["mon","tue","wed","thu","fri","sat","sun"]
def viewstudentdetails():
    for i in student_details.items():
        print(i)
    print(f"first day:{day_of_week[0]}")
    print(f"fifth day:{day_of_week[4]}")
    print(f"last day:{day_of_week[-1]}")
fruits = ["apple","mango"]
def viewfruits():
    print(fruits)
def addfruits():
    f = input("enter fruits name: ")
    fruits.append(f)
def insertfruits():
    f = input("enter fruits name: ")
    fruits.insert(0,f)
def removefruits():
    f = input("enter fruits name: ")
    if f in fruits:
        fruits.remove(f)
    else:
        print(f"{f} not available")
def addmultiplefruits():
    f = input("enter fruits seperate by space: ").split()
    fruits.extend(f)

def repeatfruits():
    while True:
        try:
            n = int(input("enter a number for how many type you want repeat: "))
            print(n * fruits)
            break
        except ValueError:
            print("value error")

l = [13,4,5,3,5,7,4,3,2]
def numberopertions():
    print(f"reverse list:{list(reversed(l))}")
    print(f"sorted list ascending:{list(sorted(l))}")
    print(f"sorted list descending:{list(sorted(l,reverse=True))}")
    print(f"Count occurrences of number 1:{l.count(1)}")
    print(f"Check if 1 exists in the list:{1 in l}")
def extranumberanalysis():
    num = []
    number = input("enter multiple number sepreated by space: ").split()
    for i in number:
        try:
             num.append(float(i))
        except ValueError:
             print(f"value error")
    if num:
        print(f"Minimum value:{min(num)}")
        print(f"Maximum value:{max(num)}")
        print(f"Sum:{sum(num)}")
        print(f"Average:{sum(num) / len(num)}")
t = (1,2,3,4,5)
def tupledemonstration():
    print(f"Count occurrences of 1:{t.count(1)}")
    print(f"Find index of 4:{t.index(4)}")
    print(f"minimum:{min(t)}")
    print(f"maximum:{max(t)}")
    print(f"sum of elements:{sum(t)}")
def main():
    while True:
        print("""
1. Student Marks Report
2. View Student Info
3. View Fruits
4. Add Fruit
5. Insert Fruit
6. Remove Fruit
7. Add Multiple Fruits
8. Repeat Fruits
9. Number Operations
10. Extra Number Analysis
11. Tuple Demonstration
12. Exit
""")
        while True:
            try:
                choice = int(input("enter choice from 1 to 12: "))
                break
            except ValueError:
                print("error value")
        if choice == 1:
            studentmarksreport()
        elif choice == 2:
            viewstudentdetails()
        elif choice == 3:
            viewfruits()
        elif choice == 4:
            addfruits()
        elif choice == 5:
            insertfruits()
        elif choice == 6:
            removefruits()
        elif choice == 7:
            addmultiplefruits()
        elif choice == 8:
            repeatfruits()
        elif choice == 9:
            numberopertions()
        elif choice == 10:
            extranumberanalysis()
        elif choice == 11:
            tupledemonstration()
        elif choice == 12:
            print("exit")
            break
        else:
            print("choice from 1 to 12")









