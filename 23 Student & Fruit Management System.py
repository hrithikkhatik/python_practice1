student_info = {"name": None, "age": None, "percentage": None}
fruits = ["Apple", "Mango", "Papaya", "Banana"]
extra_fruits = ["Watermelon", "Orange"]
days_of_week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
numbers = [0, 1, 3, 4, 1, 0, 5, 0, 0, 3, 0]
nums = [4, 9, 0, 1, 2, 8]
language = ["python", "java", "c++", "python"]
def StudentMarksReport():
    student_name = input("enter student name: ")
    age = float(input("enter age: "))
    marks1 = float(input("enter marks of subject1: "))
    marks2 = float(input("enter marks of subject2: "))
    marks3 = float(input("enter marks of subject3: "))
    total_marks = marks1 + marks2 + marks3
    percentage = total_marks / 3
    grade = "C"
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    print(f"grade:{grade}")
    student_info["name"] = student_name
    student_info["age"] = age
    student_info["percentage"] = percentage
def ViewStudentInfoDaysOfWeek():
    print(f"the student’s name, age, and percentage:{student_info['name']},{student_info['age']},{student_info['percentage']}")

print(f"First day:{days_of_week[0]}")
print(f"Fifth day:{days_of_week[4]}")
print(f"last day:{days_of_week[-1]}")
print(f"Total number of days:{len(days_of_week)}")
try:
    print(days_of_week[20])
except IndexError:
    print("index out of range")

def ViewFruits():
    print(fruits)

def AddFruit():
    f = input("Add a single fruit to the list: ")
    fruits.append(f)
    print(f"{f} add successfully")

def InsertFruit():
    index= int(input("Insert a fruit at a specific index. :"))
    f = input("enter fruit: ")
    fruits.insert(index,f)

def Combine_With_Extra_Fruits():
    fruits.extend(extra_fruits)

def Repeat_Fruits():
    n = int(input("enter n: "))
    print(fruits * n)

def Remove_Fruit():
    f = input("enter fruit to remove: ")
    if f in fruits:
        fruits.remove(f)
    else:
        print(f"{f} is not found")
def Add_Multiple_Fruits():
    f = input("enter Add multiple fruits entered by the user (space-separated).: ").split()
    fruits.extend(f)

def List_Operations():
    print(days_of_week)
    days_of_week.reverse()
    print(days_of_week)
    nums.sort()
    print(nums)
    nums.sort(reverse=True)
    print(nums)
    print(numbers)
    print(numbers.count(0))
    print("python" in language)
    print("python" not in language)
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
11. Exit
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
            print("exit")
            break
        else:
            print("enter valid choice")