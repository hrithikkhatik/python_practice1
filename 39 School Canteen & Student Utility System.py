student_details = {"name":None,"roll":None,"balance":None}
def add_student():
    name = input("enter student name: ")
    student_details["name"] = name
    while True:
        try:
            rollno = int(input("enter roll no: "))
            student_details["roll"] = rollno
            break
        except ValueError:
            print("value error")
    while True:
        try:
            balance = float(input("enter wallet balance: "))
            student_details["balance"] = balance
            break
        except ValueError:
            print("value error")
def viewstudents():
    for a,b in student_details.items():
        print(a,b)
fooditems = ["apple","mango"]
def viewfoodsitems():
    print(fooditems)
def addfooditems():
    food = input("enter food items: ")
    fooditems.append(food)
def insertfooditems():
    food = input("enter food items: ")
    fooditems.insert(0,food)
def removefooditems():
    food = input("enter food name to remove: ")
    if food in fooditems:
        fooditems.remove(food)
    else:
        print("no food of that name")
def addmultiplefood():
    food = input("enter food item to add: ").split()
    fooditems.extend(food)
daily_sales = [10000,30000,2000]
def dailysalesoperations():
    print(f"sales in reverse order:{list(reversed(daily_sales))}")
    print(f"sales in ascending order:{list(sorted(daily_sales))}")
    print(f"sales in descending order:{list(sorted(daily_sales,reverse=True))}")
    print(f"Count occurrences of a given sales value:{daily_sales.count(10)}")
salesvalue = []
def customsalesanalysis():
    while True:
        try:
            sales = input("enter sales value space sepreated: ").split()
            salesvalue.extend([float(s) for s in sales])
            break
        except ValueError:
            print("value error")
    print(f"Minimum sale value:{min(salesvalue)}")
    print(f"Maximum sale value:{max(salesvalue)}")
    print(f"Total sales sum:{sum(salesvalue)}")
    print(f"Average sales value:{sum(salesvalue) / len(salesvalue)}")
rules = ("No Credit", "Maintain Cleanliness", "Fixed Prices")
def canteenrules():
    print("tuple are immutable.rules cannot be change")
def uniquefooditems():
    food = input("Accept a list of food items (comma-separated) from the user.").split(",")
    s = set(food)
    print(f"Original number of items:{len(food)}")
    print(f"Unique items:{s}")
    print(f"Count of unique items:{len(s)}")
def main():
    while True:
        try:
            choice = int(input("enter choice: "))
        except ValueError:
            print("value error")
            break
        if choice == 1:
            add_student()
        elif choice == 2:
            viewstudents()
        elif choice == 3:
            viewfoodsitems()
        elif choice == 4:
            addfooditems()
        elif choice == 5:
            insertfooditems()
        elif choice == 6:
            removefooditems()
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
            print("break")
            break
        else:
            print("kindly enter valid number")


