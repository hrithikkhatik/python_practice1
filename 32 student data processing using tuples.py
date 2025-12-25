student_details1 = (1001,"john")
student_details2 = (78.5, 91.0, 83.5, 79.5)
student_details = student_details1 + student_details2
print(student_details)
t1 = ("Class 5", 5000)
print(t1 * 3)
print(91.0 in student_details2)
print(99.0 in student_details2)

print(91.0 not in student_details2)
print(99.0 not in student_details2)

t1 = (10, 4, 1, 9, 0, 3, 1)
print(t1.count(t1))

print(t1.index(4))
print(t1.index(10))
print(t1.index(1))

print(min(t1))
print(max(t1))
print(sum(t1))
