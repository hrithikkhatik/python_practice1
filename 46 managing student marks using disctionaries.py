student_1 = {"maths":100,"english":100,"physics":100}
student_2 = {"maths":105,"english":105,"physics":105}
print(student_1["physics"])
print(student_2["physics"])
print(student_1.get("physics"))
print(student_2.get("physics"))
#print(student_1["chem"])
#print(student_2["chem"])
print(student_1.get("chem"))
print(student_2.get("chem"))
student_1["chem"] = 100
student_2["chem"] = 105
print("bio" in student_1)
new_marks = {"maths":105,"bio":105}
student_1.update(new_marks)
student_1.pop("english")
print(student_1)
print(student_2)
