
student_details = {"name":None,"rollno":None,"accountbalance":None}
def StudentManagementModule():
    def addstudentdetails():
        studentname = input("enter student name: ")
        while True:
            try:
                rollno = int(input("enter roll no: "))
                break
            except ValueError:
                print("value error")
        while True:
            try:
                accountbalance = float(input("enter account balance: "))
                break
            except ValueError:
                print("value error")
        student_details.update({"name":studentname,"rollno":rollno,"accountbalance":accountbalance})
    def viewstudentdetails():
        for keys,values in student_details.items():
            print(f"{keys}:{values}")
    while True:
        try:
            choices = int(input("enter choice from 1 to 3: "))
        except ValueError:
            print("value error")
            continue
        if choices == 1:
            addstudentdetails()
        elif choices == 2:
            viewstudentdetails()
        elif choices == 3:
            print("exit")
            break
        else:
            print("kindly enter choice from 1 to 3")

foods = []
def FoodManagementModule():
    def addfood():
        f = input("enter food  item to add: ")
        foods.append(f)
    def insertfood():
        f = input("enter food  item to add: ")
        foods.insert(0,f)
    def removefoods():
        f = input("enter food  item to add: ")
        if f in foods:
            foods.remove(f)
        else:
            print("no food available")
    def multiplefoods():
        f = input("enter food with space seprated: ").split()
        foods.extend(f)
    def viewfoods():
        print(f"all foods:{foods}")
    while True:
        try:
            choice = int(input("enter choice from 1 to 6: "))
        except ValueError:
            print("value error")
            continue
        if choice == 1:
            addfood()
        elif choice == 2:
            insertfood()
        elif choice == 3:
            removefoods()
        elif choice == 4:
            multiplefoods()
        elif choice == 5:
            viewfoods()
        elif choice == 6:
            print("exit")
            break
        else:
            print("kindly enter a valid choice")
dailysales = [34,5325,2456,7543,7354,234,12]
def SalesAnalysisModule():
    print(f"Reverse order:{list(reversed(dailysales))}")
    print(f"Ascending order:{list(sorted(dailysales))}")
    print(f"Descending order:{list(sorted(dailysales,reverse=True))}")
    customsales = input("enter sales value space seprated: ").split()
    sales = []
    for i in customsales:
        try:
            sales.append(float(i))
        except ValueError:
            print(f"value error:{i}")
    if len(sales) == 0:
        print("no valid sales")
        return
    print(f"Minimum sale:{min(sales)}")
    print(f"Maximum sale:{max(sales)}")
    print(f"Total sales:{sum(sales)}")
    print(f"Average sales:{sum(sales) / len(sales)}")
def SetOperationsModule():
    food = input("enter food space seprated: ").split()
    print(f"unique food items:{set(food)}")
    group1 = input("enter subject of group1 with space").split()
    group2 = input("enter subject of group2 with space").split()
    group3 = input("enter subject of group3 with space").split()
    group1 = set(group1)
    group2 = set(group2)
    group3 = set(group3)
    print(f"common subjects between Group 1 and Group 2:{group1.intersection(group2)}")
    print(f"subjects common to all three groups:{group1.intersection(group2,group3)}")
    print(f"all unique subjects across groups:{group1.union(group2,group3)}")
    group1 = frozenset(group1)
    group2 = frozenset(group2)
    group3 = frozenset(group3)
    print(f"subjects common to all three groups:{group1.intersection(group2, group3)}")
    print(f"common subjects between Group 1 and Group 2:{group1.intersection(group2)}")
    print(f"Difference:{group1-group2}")
def GroceryManagementModule():
    grocery_items = {"apple":100,"mango":200}
    def Viewallgroceryitems():
        print(f"all grocery items:{grocery_items}")
    def checkpriceofitem():
        checkprice = input("enter item name to check its price: ")
        if checkprice in grocery_items:
            print(f"check price of specific item:{grocery_items[str(checkprice)]}")
        else:
            print("no item of that name")
    def updateprice():
        item = input("enter item name to update price: ")
        while True:
            try:
                price = int(input(f"enter price to update price of {item}"))
                grocery_items[str(item)] = price
                break
            except ValueError:
                print("value error")

    def addgroceryitem():
        additem = input("enter item name to add: ")
        while True:
            try:
                price = int(input(f"enter item name to price of {additem}: "))
                grocery_items[str(additem)] = price
                break
            except ValueError:
                print("value error")
    def deleteitem():
        deleteitem = input("enter a item to delete")
        if deleteitem in grocery_items:
            del grocery_items[str(deleteitem)]
        else:
            print("no item available")
    while True:
        try:
            choices = int(input("enter choice from 1 to 6: "))
        except ValueError:
            print("value error")
            continue
        if choices == 1:
            Viewallgroceryitems()
        elif choices == 2:
            checkpriceofitem()
        elif choices == 3:
            updateprice()
        elif choices == 4:
            addgroceryitem()
        elif choices == 5:
            deleteitem()
        elif choices == 6:
            print("exit")
            break
        else:
            print("kindly enter choice from 1 to 6")
def main():
    while True:
        try:
            choices = int(input("enter choice from 1 to 6"))
        except ValueError:
            print("value error")
            continue
        if choices == 1:
            StudentManagementModule()
        elif choices == 2:
            FoodManagementModule()
        elif choices == 3:
            SalesAnalysisModule()
        elif choices == 4:
            SetOperationsModule()
        elif choices == 5:
            GroceryManagementModule()
        elif choices == 6:
            print("exit")
            break
        else:
            print("kindly enter from 1 to 6")













