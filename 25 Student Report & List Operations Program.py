student_info = {
    "name": None,
    "age": None,
    "percentage": None
}
def StudentMarksReport():
    name = input("enter name: ")
    age = int(input("enter age: "))
    marks1 = float(input("enter Marks of subject1: "))
    marks2 = float(input("enter marks of subject2: "))
    marks3 = float(input("enter marks of subject3: "))
    total_marks = marks1 + marks2 + marks3
    percentage = total_marks / 3
    Grade = "C"
    if percentage >= 90:
        Grade = "A+"
    elif percentage >= 75:
        Grade = "A"
    elif percentage >= 60:
        Grade = "B"
    print(f"grade:{Grade}")
    student_info["name"] = name
    student_info["age"] = age
    student_info["percentage"] = percentage


days_of_week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
def ViewStudentInfoDaysOfWeek():
    global days_of_week
    print(f"Stored student information:{student_info['name']},{student_info['age']},{student_info['percentage']}")
    print(f"First day of the week:{days_of_week[0]}")
    print(f"Fifth day:{days_of_week[4]}")
    print(f"Last day:{days_of_week[-1]}")
    print(f"Total number of days:{len(days_of_week)}")
    try:
        index = int(input("enter index value: "))
        print(f"{days_of_week[index]}")
    except ValueError:
        print("value error")
    except IndexError:
        print("index error")

fruits = ["Apple", "Mango", "Papaya", "Banana"]
extra_fruits = ["Watermelon", "Orange"]
def ViewFruits():
    print(fruits)

def AddFruit():
    f = input("enter fruit name: ")
    fruits.append(f)

def InsertFruit():
    I = int(input("enter index: "))
    f = input("enter fruit name: ")
    fruits.insert(I,f)

def Combine_With_Extra_Fruits():
    fruits.extend(extra_fruits)

def Repeat_Fruits():
    n = int(input("enter n: "))
    print(n * fruits)

def Remove_Fruit():
    f = input("enter fruit name: ")
    if f in fruits:
        fruits.remove(f)
    else:
        print("fruit does not exit")

def Add_Multiple_Fruits():
    f = input("enter space separated fruits: ").split()
    fruits.extend(f)

numbers = [0, 1, 3, 4, 1, 0, 5, 0, 0, 3, 0]
nums = [4, 9, 0, 1, 2, 8]
language = ["python", "java", "c++", "python"]
def List_Operations():
    days_of_week.reverse()
    print(days_of_week)
    nums.sort()
    print(nums)
    nums.sort(reverse=True)
    print(nums)
    print(numbers.count(0))

    print("python" in language)

def ExtraProgram():
    number = input("enter comma separated number: ").split(",")
    items = []
    for item in number:
        item = item.strip()
        try:
            a = float(item)
            items.append(a)
        except ValueError:
            print(f"Ignored non-numeric value: {item}")

    if items:
        print(f"List of valid numbers:{items}")
        print(f"Smallest value:{min(items)}")
        print(f"Largest value:{max(items)}")
        print(f"Sum:{sum(items)}")
        print(f"Average:{sum(items) / len(items)}")
        print(f"Count of valid numbers:{len(items)}")

def main():
    while True:
        print("""
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
11. ExtraProgram
12. Exit
""")
        choice = int(input("enter choice: "))
        if choice == 1:
            StudentMarksReport()
        elif choice == 2:
            ViewStudentInfoDaysOfWeek()
        elif choice == 3:
            ViewFruits()
        elif choice == 4:
            AddFruit()
        elif choice == 5:
            InsertFruit()
        elif choice == 6:
            Combine_With_Extra_Fruits()
        elif choice == 7:
            Repeat_Fruits()
        elif choice == 8:
            Remove_Fruit()
        elif choice == 9:
            Add_Multiple_Fruits()
        elif choice == 10:
            List_Operations()
        elif choice == 11:
            ExtraProgram()
        elif choice == 12:
            print("exit")
            break
        else:
            print("no option available")


