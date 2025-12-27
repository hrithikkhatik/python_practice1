s1 = "python is fun"
s2 = s1.replace("python", "java")
print(s1)
print(s2)
s3 = s1.capitalize()
print(s3)

t1 = ("mango", "orange", "apple")
l = list(t1)
l.append("banana")
l[0] = "banana"


l1 = ["mango", "orange", "apple"]
print(id(l1))
l.append("banana")
print(id(l1))
l1[-1] = "grapes"

print("""
| Data Type | Mutable? | Can Change Elements? | Memory Behavior |
| --------- | -------- | -------------------- | --------------- |
| String    | no        | no                   | different    |
| Tuple     | no        | no                    | different    |
| List      | yes       | yes                    | same         |
""")

