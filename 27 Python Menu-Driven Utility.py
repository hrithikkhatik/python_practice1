student_information = {"name":None,"age":None,"percentage":None}
def StudentMarksReport():
    name = input("enter name: ")
    while True:
        try:
            age = int(input("enter age: "))
            subject = int(input("enter total subject: "))
            break
        except ValueError:
            print("value error")
    marks = []
    for i in range(subject):
        a = float(input(f"enter Marks for subject{i+1}: "))
        marks.append(a)
    Total_marks = sum(marks)
    percentage = Total_marks / subject
    grade = "C"
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    print(f"grade:{grade}")
    student_information["name"] = name
    student_information["age"] = age
    student_information["percentage"] = percentage
day_of_week = ["mon","tue","wed","thu","fri","sat","sun"]
def ViewStudentInfoDaysOfWeek():
    print(f"name,age,percentage:{student_information["name"]},{student_information["age"]},{student_information["percentage"]}")
    print(f"First day:{day_of_week[0]}")
    print(f"Fifth day:{day_of_week[4]}")
    print(f"Last day:{day_of_week[-1]}")
    print(f"Total number of days:{len(day_of_week)}")
    Index = int(input("enter an index: "))
    try:
        print(day_of_week[Index])
    except ValueError:
        print("error enter correct value")
    except IndexError:
        print("error enter valid index")
fruits = ["apple","mango","orange"]
def view_fruits():
    print(fruits)
def add_fruits():
    f = input("enter fruit: ")
    fruits.append(f)

def insert_fruits():
    try:
        Index = int(input("enter index: "))
    except IndexError:
        print("index error")
    except ValueError:
        print("error value")

    f = input("enter fruit: ")
    fruits.insert(Index,f)

def combine_extra_fruits():
    extra_list = []
    f = input("enter fruits space separated").split()
    extra_list.extend(f)
    fruits.extend(extra_list)
def repeat_fruit():
    n = int(input("enter n: "))
    print(n * fruits)

def remove_fruits():
    f = input("enter fruit to remove: ")
    if f in fruits:
        fruits.remove(f)
    else:
        print("no fruits available")

def add_multiple_fruits():
    fr = []
    f = input("enter fruits space separated").split()
    fr.extend(f)
    fruits.extend(fr)
numbers = [1,3,2,5,-1,1]
n = 1
def ListOperations():
    print(f"Reverse the list of days of the week:{reversed(day_of_week)}")
    print(f"Sort a list of numbers in ascending and descending order:{list(sorted(numbers))},{list(sorted(numbers,reverse=True))}")
    print(f"Count occurrences of a specific number in another list:{print(numbers.count(n))}")
    print(f"Check if a particular element exists in a list:{n in numbers}")

def ExtraNumberAnalysis():
    number = input("input comma-separated numbers: ").split(",")
    items = []
    for item in number:
        item.strip()
        try:
            a = float(item)
            items.append(a)
        except ValueError:
            print(f"Filter out invalid (non-numeric) inputs:{item}")
    print(f"Smallest number:{min(items)}")
    print(f"Largest number:{max(items)}")
    print(f"Sum:{sum(items)}")
    print(f"Average:{sum(items) / len(items)}")
    print(f"Count of valid numbers:{len(items)}")
def main():
    while True:
        print("""
========= MENU =========
1. Student Marks Report
2. View Student Info & Days of Week
3. View Fruits
4. Add Fruit
5. Insert Fruit
6. Combine With Extra Fruits
7. Repeat Fruits
8. Remove Fruit
9. Add Multiple Fruits
10. List Operations
11. Extra Number Analysis
12. Exit
========================
""")
        try:
            choice = int(input("enter choice: "))
        except ValueError:
            print("error enter int")
        if choice == 1:
            StudentMarksReport()
        elif choice == 2:
            ViewStudentInfoDaysOfWeek()
        elif choice == 3:
            view_fruits()
        elif choice == 4:
            add_fruits()
        elif choice == 5:
            insert_fruits()
        elif choice == 6:
            combine_extra_fruits()
        elif choice == 7:
            repeat_fruit()
        elif choice == 8:
            remove_fruits()
        elif choice == 9:
            add_multiple_fruits()
        elif choice == 10:
            ListOperations()
        elif choice == 11:
            ExtraNumberAnalysis()
        elif choice == 12:
            print("break")
            break
        else:
            print("error enter valid option from 1 to 12")









