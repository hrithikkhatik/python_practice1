student_details = {"studentname":None,"rollno":None,"accountbalance":None}
def addstudent():
    student_name = input("enter student name: ")
    while True:
        try:
            rollno = int(input("enter student rollno: "))
            break
        except ValueError:
            print("kindly enter a numeric value")
    while True:
        try:
            account_balance = float(input("enter account balance: "))
            break
        except ValueError:
            print("kindly enter a numeric value")
    student_details.update({"studentname":student_name,"rollno":rollno,"accountbalance":account_balance})
def viewstudents():
    for keys,values in student_details.items():
        print(keys , values)
foods = []
def viewfoods():
    print(foods)
def addfoods():
    f = input("enter a food: ")
    foods.append(f)
def insertfoods():
    f = input("enter a food: ")
    foods.insert(0,f)
def removefoods():
    f = input("enter food name to remove: ")
    if f in foods:
        foods.remove(f)
    else:
        print("there is no food of that name")
def addmultiplefood():
    f = input("enter food item to add with space seprated: ").split()
    foods.extend(f)
dailysales = [737,8237,63870,6347]
def dailysalesoperations():
    print(f"sales in reverse order:{list(reversed(dailysales))}")
    print(f"sales in ascending order:{list(sorted(dailysales))}")
    print(f"sales in descending order:{list(sorted(dailysales,reverse=True))}")
def customsalesanalysis():
    sales = input("enter sales value to analysis: ").split()
    finalsales = []
    for i in sales:
        try:
            finalsales.append(float(i))
        except:
            print(f"{i} are string")
    print(f"Minimum sales:{min(finalsales)}")
    print(f"Maximum sales:{max(finalsales)}")
    print(f"Total sales:{sum(finalsales)}")
    print(f"Average sales:{sum(finalsales) / len(finalsales)}")
def canteenrules():
    rules = ("fixed price",)
    print(rules)
def uniquefooditems():
    food = input("enter food item seprated by space: ").split()
    print(f"unique food item:{set(food)}")
def subjectanalysis():
    group1 = input("enter subject name for group1: ").split()
    group2 = input("enter subject name for group2: ").split()
    group3 = input("enter subject name for group3: ").split()
    g1 = set(group1)
    g2 = set(group2)
    g3 = set(group3)
    print(f"Subjects common between Group 1 and Group 2:{g1.intersection(g2)}")
    print(f"Subjects common in all three groups:{g1.intersection(g2,g3)}")
    print(f"All unique subjects across all groups:{g1.union(g2,g3)}")
def systemgroupanalysis():
    groupa = frozenset({1,2,3,4})
    groupb = frozenset({2,4,3,2})
    print(f"Common elements between groups:{groupa.intersection(groupb)}")
    print(f"All unique elements:{groupa.union(groupb)}")
    print(f"Difference between Group A and Group B:{groupa-groupb}")
    print(f"Difference between Group B and Group A:{groupb-groupa}")
def main():
    while True:
        try:
            choice = int(input("enter choice from 1 to 14: "))
        except ValueError:
            print("value error")
            continue
        if choice == 1:
            addstudent()
        elif choice == 2:
            viewstudents()
        elif choice == 3:
            viewfoods()
        elif choice == 4:
            addfoods()
        elif choice == 5:
            insertfoods()
        elif choice == 6:
            removefoods()
        elif choice == 7:
            addmultiplefood()
        elif choice == 8:
            dailysalesoperations()
        elif choice == 9:
            customsalesanalysis()
        elif choice == 10:
            canteenrules()
        elif choice == 11:
            uniquefooditems()
        elif choice == 12:
            subjectanalysis()
        elif choice == 13:
            systemgroupanalysis()
        elif choice == 14:
            print("exit the program")
            break
        else:
            print("kindly enter choice from 1 to 14")
















