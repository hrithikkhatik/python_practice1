fruits = ("mango", "orange", "apple")
l = list(fruits)
l.extend(["banana","grapes"])
if "orange" in l:
    l.remove("orange")
else:
    print("orange is not available")
tup = tuple(l)
print(f"The total number of fruits {len(tup)}")
print(f"The final fruit collection:{tup}")
print(f"The first fruit in the collection:{tup[0]}")
print(f"The last fruit in the collection:{tup[-1]}")


