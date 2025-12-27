l = input("Enter elements separated by commas:").split(",")
li = []
for i in l:
    i = i.strip()
    try:
        a = int(i)
    except ValueError:
        try:
            a  = float(i)
        except ValueError:
            a = i
    li.append(a)


s1 = set(li)

print(li)
print(len(li))
print(s1)
print(len(s1))
print(li[0])
try:
    print(s1[0])
except:
    print("error")

print("set removed duplicate items automatically.")

