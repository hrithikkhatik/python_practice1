print("=== STRING IMMUTABILITY ===")
s1 = "python is fun"
print(s1)
s2 = s1.replace("python","java")
print(s1)
print(s2)

try:
    s1[0]="p"
    print(s1)
except:
    print("error")
print("=== TUPLE IMMUTABILITY ===")
t1 = ("mango", "orange", "apple")
try:
    t1.append("banana")
    print(t1)
except:
    print("error")

try:
    t1[0] = "banana"
except:
    print("error")
print("=== LIST MUTABILITY ===")
l1 = ["mango", "orange", "apple"]
print(l1)
l1.append("banana")
print(l1)
print("=== LIST MEMORY BEHAVIOR ===")
l2 = ["mango", "orange", "apple"]
print(l2)
print(id(l2))
l2.append("banana")
print(l2)
print(id(l2))
print("=== MODIFYING LIST ELEMENTS ===")
l3 = ["mango", "orange", "apple"]
print(l3[-1])
print(id(l3))
l3[-1] = "apple"
print(l3)
print(id(l3))
print("=== END OF PROJECT ===")

