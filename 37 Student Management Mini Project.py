student_details = {"name":None,"age":None,"percentage":None}
def studentmarksreport():
    name = input("enter your name: ")
    while True:
        try:
            age = int(input("enter your age: "))
            break
        except ValueError:
            print("value error")
    while True:
        try:
            numberofsubjects = int(input("enter number of subjects: "))
            break
        except ValueError:
            print("value error")
    if numberofsubjects >= 1:
        marks = []
        for i in range(numberofsubjects):
            m = float(input(f"enter marks of subject{i+1}: "))
            if 0 <=m <= 100:
                marks.append(m)
            else:
                print("marks cannot be bigger than 100")
        percentage = (sum(marks) / (numberofsubjects*100)) * 100
        student_details.update({"name":name,"age":age,"percentage":percentage})
day_of_week = ["mon","tue","wed","thu","fri","sat","sun"]
def viewstudentdetails():
    for i in student_details.items():
        print(i)
    print(f"first day:{day_of_week[0]}")
    print(f"fifth day:{day_of_week[4]}")
    print(f"last day:{day_of_week[-1]}")
fruits = ["apple"]
def viewfruits():
    print(f"view fruits:{fruits}")
def addfruits():
    f = input("enter a fruit name: ")
    fruits.append(f)
def insertfruits():
    f = input("enter fruit name to insert: ")
    fruits.insert(0,f)
def removefruits():
    f = input("enter fruit name to remove")
    try:
        fruits.remove(f)
    except:
        print(f"no fruit of that name:{f}")
def addmultiplefruits():
    fruits.extend(input("enter fruits names: ").split())
l = [1,3,4,6,7,3,2,4,6,7]
def numberoperations():
    print(f"numbers in reverse order:{list(reversed(l))}")
    print(f"Sort numbers in ascending order:{list(sorted(l))}")
    print(f"Sort numbers in descending order:{list(sorted(l,reverse=True))}")
    try:
        a = int(input("enter number to count occurences: "))
    except ValueError:
        print("value error")
    print(f"Count occurrences of a given number:{l.count(a)}")
    print(f"Check if a number exists in the list:{1 in l}")
def extranumberanalysis():
    n = []
    number = input("enter number with space sepreated: ").split()
    for i in number:
        try:
            n.append(float(i))
        except ValueError:
            print("value error")
    print(f"Minimum value:{min(n)}")
    print(f"Maximum value:{max(n)}")
    print(f"Sum of values:{sum(n)}")
    print(f"Average of values:{sum(n) / len(n)}")

def tupledemonstration():
    t = (1,2,3,4,5)
    try:
        t.append(2)
    except:
        print("error")
def setdemonstartion():
    s = input("enter comma sepreated value: ").split(",")
    se = []
    for i in s:
        try:
            se.append(float(i))
        except:
            print("error")
    sets = set(se)
    print(set)
    print(len(s))
    print(len(sets))
def main():
    while True:
        try:
            choice = int(input("enter your choice: "))
        except ValueError:
            print("value error")
            break
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
            numberoperations()
        elif choice == 9:
            extranumberanalysis()
        elif choice == 10:
            tupledemonstration()
        elif choice == 11:
            setdemonstartion()
        elif choice == 12:
            print("break")
            break
        else:
            print("enter choice from 1 to 12")
main()














