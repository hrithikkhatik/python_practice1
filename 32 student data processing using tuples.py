# Student basic details
student_basic = (1001, "John")

# Student marks in four subjects
marks = (78.5, 91.0, 83.5, 79.5)

# Class and fee details
class_fee = ("Class 5", 5000)

# Numerical tuple
numbers = (10, 4, 1, 9, 0, 3, 1)

student_record = student_basic + marks
print(student_record)

print(f"Repeat the class_fee tuple three times:{class_fee*3}")

print(f"Check whether the following numbers are present in the marks{91.0}:{91.0 in marks}")
print(f"Check whether the following numbers are present in the marks{99.0}:{99.0 in marks}")

print(f"Check whether the following numbers are not present in the marks:{91.0}:{91.0 not in marks}")
print(f"Check whether the following numbers are not present in the marks:{99.0}:{99.0 not in marks}")

print(f"Count how many times the entire tuple appears inside itself:{numbers}:{numbers.count(numbers)}")
print(f"index of {4}:{numbers.index(4)}")
print(f"index of {4}:{numbers.index(4)}")
print(f"first occurence of 1:{numbers.index(1)}")

print(f"Minimum value:{min(numbers)}")
print(f"maximum value:{max(numbers)}")
print(f"Sum of all elements:{sum(numbers)}")


