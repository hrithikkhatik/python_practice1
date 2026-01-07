student_details = {"student name":None,"rollno":None,"accountbalance":None}
def studentmanagement():
    student_name = input("enter student name: ")
    while True:
        try:
            roll_no = int(input("enter your roll no: "))
            break
        except ValueError:
            print("value error")
    while True:
        try:
            account_balance = float(input("enter account balance: "))
            break
        except ValueError:
            print("value error")
    student_details.update({"student name": student_name, "rollno": roll_no, "accountbalance": account_balance})
def viewstudents():
    for keys,values in student_details.items():
        print(keys,values)
foods = []
def allfoods():
    print(foods)
def addfoods():
    food = input("enter food item: ")
    foods.append(food)
def insertfood():
    food = input("enter food item: ")
    foods.insert(0,food)
def removefood():
    food = input("enter food item to remove: ")
    if food in foods:
        foods.remove(food)
    else:
        print(f"no food available{food}")
def addmultiple():
    food = input("enter multiple food item with space: ").split()
    foods.extend(food)
dailysales = [123828,9128,2937]
def dailysalesoperations():
    print(f"sales in reverse order is {list(reversed(dailysales))}")
    print(f"sales sorted in ascending order is {list(sorted(dailysales))}")
    print(f"sales sorted in descending order IS {list(sorted(dailysales,reverse=True))}")
def customsalesanalysis():
    s = []
    sales = input("enter sales number space sepreated: ").split()
    for i in sales:
        s.append(float(i))
    print(f"minimum sales:{min(s)}")
    print(f"maximum sales:{max(s)}")
    print(f"total sales:{sum(s)}")
    print(f"average sales:{sum(s) / len(s)}")
def canteenrules():
    t = ("No credit", "Low balance no food", "Maintain cleanliness")
    print(t)
def uniquefooditems():
    foods_items = input("enter food items space seperated: ").split()
    print(f"original count of food items is {len(foods_items)}")
    print(f"unique food items is {set(foods_items)}")
    print(f"count of unique food items is {len(set(foods_items))}")
def subjectanalysisusingsets():
    group1 = set(input("enter subjects of group 1: ").split())
    group2 = set(input('enter subjects of group 2: ').split())
    group3 = set(input('enter subjects of group 3: ').split())
    print(f"common subjects between Group 1 and Group 2 is {group1 & group2}")
    print(f"subjects common to all three groups is {group1 & group2 & group3}")
    print(f"all subjects offered across the three groups:{group1},{group2},{group3}")
def main():
    while True:
        try:
            choice = int(input("enter choice: "))
        except ValueError:
            print("value error")
            continue
        if choice == 1:
            studentmanagement()
        elif choice == 2:
            viewstudents()
        elif choice == 3:
            allfoods()
        elif choice == 4:
            addfoods()
        elif choice == 5:
            insertfood()
        elif choice == 6:
            removefood()
        elif choice == 7:
            addmultiple()
        elif choice == 8:
            dailysalesoperations()
        elif choice == 9:
            customsalesanalysis()
        elif choice == 10:
            canteenrules()
        elif choice == 11:
            uniquefooditems()
        elif choice == 12:
            subjectanalysisusingsets()
        elif choice == 13:
            print("break")
            break
        else:
            print("value error")
main()

