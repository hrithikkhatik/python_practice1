number = input("Prompt the user to enter several values separated by commas (,): ").split(",")
items = []
for item in number:
    try:
        a = float(item)
        items.append(a)
    except ValueError:
        print(f"Ignored non-numeric value:{item.strip()}")
if items:
    print(f"numbers:{items}")
    print(f"Smallest number:{min(items)}")
    print(f"Largest number:{max(items)}")
    print(f"Total sum:{sum(items)}")
    print(f"Average:{sum(items) / len(items)}")
    print(f"Count of valid numbers:{len(items)}")
else:
    print("No valid numbers provided.")

