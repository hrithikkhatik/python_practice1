student_info = {"name": None, "age": None, "percentage": None}
def student_marks_report():
    StudentName = input("Enter Student Name: ")
    Age = float(input("Enter Age: "))
    Marks1 = float(input("Enter Marks of subject1:"))
    Marks2 = float(input("Enter Marks of subject2:"))
    Marks3 = float(input("Enter Marks of subject3:"))
    TotalMarks = Marks1 + Marks2 + Marks3
    Percentage = TotalMarks / 3
    Grade = "C"
    if Percentage >= 90:
        Grade = "A+"
    elif Percentage >= 75:
        Grade = "A"
    elif Percentage >= 60:
        Grade = "B"
    print(f"percentage and grade:{Percentage},{Grade}")
    student_info["name"] = StudentName
    student_info["age"] = Age
    student_info["percentage"] = Percentage

def view_student_info_days_of_week():
    if student_info["name"] is None:
        print("please enter option 1")
        return
    print(f"Student Name:{student_info['name']}")
    print(f"Age:{student_info['age']}")
    print(f"Percentage:{student_info['percentage']}")
    Week_Day = ["mon","tue","wed","thu","fri","sat","sun"]
    print(f"First day:{Week_Day[0]}")
    print(f"Fifth day:{Week_Day[4]}")
    print(f"Last day:{Week_Day[-1]}")
    print(f"the total number of days:{len(Week_Day)}")
    try:
        print(Week_Day[8])
    except IndexError:
        print("Index out of range")

fruits = ["Apple", "Mango", "Papaya", "Banana"]
extra_fruits = ["Watermelon", "Orange"]
def view_fruits():
    print(fruits)

def add_fruit():
    fruit = input("Enter fruit")
    fruits.append(fruit)

def add_multiple():
    fruit = input("Enter fruit list separated by space:").split()
    fruit_list = []
    for i in fruit:
        fruit_list.append(i)
    fruits.extend(fruit_list)

def insert_fruit():
    Fruit_name = input("Enter Fruit name: ")
    Index = int(input("Enter Index at which to insert: "))
    fruits.insert(Index,Fruit_name)


def combine_extra_fruits():
    fruits.extend(extra_fruits)

def repeat_fruits():
    n = int(input("Enter a number n: "))
    print(fruits * n)

def remove_fruit():
    fruit_name = input("Enter fruit name: ")
    if fruit_name in fruits:
        fruits.remove(fruit_name)
    else:
        print("fruit is not available")
print("""
--- STUDENT UTILITIES ---
1. Student Marks Report
9. View Student Info & Days of Week

--- FRUIT BASKET MANAGER ---
10. View Fruits
11. Add Fruit
12. Insert Fruit
13. Combine With Extra Fruits
14. Repeat Fruits
16. Remove Fruit
17. Add Multiple Fruits

15. Exit
""")
def Main():
    while True:
        choice = int(input("Enter Choice: "))
        if choice == 1:
            student_marks_report()
        elif choice == 9:
            view_student_info_days_of_week()
        elif choice == 10:
            view_fruits()
        elif choice == 11:
            add_fruit()
        elif choice == 12:
            insert_fruit()
        elif choice == 13:
            combine_extra_fruits()
        elif choice == 14:
            repeat_fruits()
        elif choice == 16:
            remove_fruit()
        elif choice == 17:
            add_multiple()
        elif choice == 15:
            print("exit")
            break
        else:
            print("Enter Valid Choice")

Main()