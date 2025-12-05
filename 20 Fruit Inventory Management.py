Fruits = ["apple", "mango", "orange"]
def show_inventory():
    print(f"Current inventory:{Fruits}")
    print(f"Total fruits:{len(Fruits)}")
def add_fruit(fruit):
    Fruits.append(fruit)

def add_multiple(fruit_list):
    Fruits.extend(fruit_list)

def remove_fruit(fruit):
    if fruit in Fruits:
        Fruits.remove(fruit)
    else:
        print(f"{fruit} not found!")





