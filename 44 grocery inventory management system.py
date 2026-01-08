
groceries = {
    "milk": 60,
    "biscuits": 20,
    "rice": 90,
    "bread": 30
}

def View_all_items():
    print(groceries)

def CheckPriceOfAnItem():
    item = input("enter a item name to check price: ").lower()
    if item in groceries:
        print(groceries[item])
    else:
        print(f"{item} is not available")

def UpdatePriceOfAnItem():
    item = input("enter item name for update price: ").lower()
    if item in groceries:
        try:
            new_price = int(input("enter new price: "))
            groceries[item] = new_price
        except ValueError:
            print("value error enter a int or float number not a alphabet")
    else:
        print(f"{item} is not available")

def AddANewItem():
    item = input("enter item name for add a new item: ").lower()
    if item not in groceries:
        try:
            price = int(input("enter a price for new item: "))
            groceries[item] = price
        except ValueError:
            print("value error enter a int or float number not a alphabet")
    else:
        print(f"{item} already exist")



def DeleteAnItem():
    item = input("enter a item name for delete: ").lower()
    if item in groceries:
        del groceries[item]
    else:
        print(f"{item} is not available")

def main():
    while True:
        print("""
--- Grocery Inventory Menu ---
1. View all items
2. Check price of an item
3. Update price of an item
4. Add a new item
5. Delete an item
6. Exit
""")
        try:
            choice = int(input("enter choice from 1 to 6"))
        except ValueError:
            print("error enter int number from 1 to 6")
            continue
        if choice == 1:
            View_all_items()
        elif choice == 2:
            CheckPriceOfAnItem()
        elif choice == 3:
            UpdatePriceOfAnItem()
        elif choice == 4:
            AddANewItem()
        elif choice == 5:
            DeleteAnItem()
        elif choice == 6:
            print("exit")
            break
        else:
            print("choice out of range")

main()