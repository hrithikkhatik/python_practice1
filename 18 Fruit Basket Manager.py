fruits = ["Apple", "Banana"]
extra_fruits = ["Orange", "Grape"]
def ViewFruits():
    print(f"the current fruits list.:{fruits}")
def AddFruit():
    FruitName = input("enter a fruit name.: ")
    fruits.append(FruitName)
    print(fruits)
def InsertFruit():
    FruitName = input("Enter Fruit Name: ")
    Index = int(input("Enter Index: "))
    fruits.insert(Index,FruitName)
    print(fruits)
def CombineWithExtraFruits():
    fruits.extend(extra_fruits)
    print(fruits)
def RepeatFruits():
    Repeat = int(input("Enter how many times they want to repeat the list.: "))
    print(fruits * Repeat)
def Main():
    while True:
        print("""Fruit Basket Manager
        1. View Fruits
        2. Add Fruit
        3. Insert Fruit
        4. Combine with Extra Fruits
        5. Repeat Fruits
        6. Exit
        """)
        Choice = int(input("Enter Choice From 1 to 6: "))
        if Choice == 1:
            ViewFruits()
        elif Choice == 2:
            AddFruit()
        elif Choice == 3:
            InsertFruit()
        elif Choice == 4:
            CombineWithExtraFruits()
        elif Choice == 5:
            RepeatFruits()
        elif Choice == 6:
            print("you successfully terminate program")
            break
        else:
            print("Invalid choice! Try again.")
Main()
