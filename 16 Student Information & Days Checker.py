Name = input("Enter Name: ")
Age = float(input("Enter Age: "))
Percentage = float(input("Enter Percentage: "))
Student = [Name, Age ,Percentage]
print("=== STUDENT INFORMATION ===")
print(type(Student))
print(Student)
days_of_week = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
print(f"The first day:{days_of_week[0]}")
print(f"The fifth day:{days_of_week[4]}")
print(f"The last day:{days_of_week[6]}")
print(f"The total number of days:{len(days_of_week)}")
print(f"The last day using negative index:{days_of_week[-1]}")

try:
    print(days_of_week[8])
except IndexError:
    print("Error: Index 8 does not exist in days_of_week!")