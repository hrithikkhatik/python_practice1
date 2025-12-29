Student1 = {"english", "maths", "cs", "chemistry", "physics"}
Student2 = {"english", "biology", "chemistry", "physics"}
Student3 = {"sanskrit", "maths", "cs"}

common_subjects = Student1.intersection(Student2)
print(common_subjects)

common_subjects = Student1.intersection(Student2,Student3)
print(common_subjects)

all_subjects = Student1.union(Student2,Student3)
print(all_subjects)

common_subjects = Student1 & Student2
print(common_subjects)

common_subjects = Student1 & Student2 & Student3
print(common_subjects)

all_subjects = Student1 | Student2
print(all_subjects)

all_subjects = Student1 | Student2 | Student3
print(all_subjects)

days = {"mon", "tue", "wed", "thu", "fri"}
weekend = {"sat", "sun"}

print(days - weekend)
print(days.difference(weekend))




