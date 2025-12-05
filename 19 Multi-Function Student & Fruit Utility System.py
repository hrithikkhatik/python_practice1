
name = None
age = None
percentage = None

def StudentMarksReport():
    global name,age,percentage
    Name = input("Enter Name: ")
    Age = float(input("Enter Age: "))
    ProgrammingLanguage = input("Enter Programming language: ")
    StudyHours = float(input("Enter Study hours: "))
    Marks1 = float(input("Enter Marks for subjects1: "))
    Marks2 = float(input("Enter Marks for subjects2: "))
    Marks3 = float(input("Enter Marks for subjects3: "))
    TotalMarks = Marks1 + Marks2 + Marks3
    Percentage = TotalMarks / 3
    if Percentage >= 90:
        print("Grade:A+")
    elif Percentage >= 75:
        print("Grade:A")
    elif Percentage >= 60:
        print("Grade:B")
    elif Percentage < 60:
        print("Grade:C")
    name = Name
    age = Age
    percentage = Percentage
def TemperatureConversion():
    print("1.Celsius → Fahrenheit")
    print("2.Fahrenheit → Celsius")
    def CelsiusToFahrenheit():
        Celsius = float(input("Enter Temperature In Celsius: "))
        Fahrenheit = (Celsius * 9 / 5) + 32
        print(f"Temperature Celsius To Fahrenheit:{Fahrenheit}")
    def FahrenheitToCelsius():
        Fahrenheit = float(input("Enter Temperature In Fahrenheit:"))
        Celsius = (Fahrenheit - 32) * 5 / 9
        print(f"Temperature Fahrenheit To Celsius:{Celsius}")
    Choice = int(input("Enter Choice From 1 to 2:"))
    if Choice == 1:
        CelsiusToFahrenheit()
    elif Choice == 2:
        FahrenheitToCelsius()
    else:
        print("Choice Error")
def SimpleInterestCalculator():
    Principal = float(input("Enter Principal Amount: "))
    Rate = float(input("Enter Rate of interest: "))
    Time = float(input("Enter Time: "))
    SimpleInterest = (Principal * Rate * Time) / 100
    print(f"Simple Interest Is:{SimpleInterest}")
def MathOperations():
    Numbers = input("Enter Number Separated By Space: ").split()
    Nums = []
    for i in Numbers:
        a = float(i)
        Nums.append(a)
    print(f"Maximum and minimum is:{max(Nums)},{min(Nums)}")
    number = float(input("Enter Number for Absolute value: "))
    print(f"Absolute value of a number:{abs(number)}")
    Base = float(input("Enter Base Value: "))
    Exponent = float(input("Enter Exponent Value: "))
    print(f"Base to Exponent Is:{pow(Base,Exponent)}")
def StringOperations():
    String = "Hello World"
    print(f"Length Is:{len(String)}")
    print(f"First and last character:{String[0]},{String[-1]}")
    print(f"Data type:{type(String)}")
    print("H\nK")
    print("H\"K")
    print("H\'K")
    print("H\\K")
def EscapeCharacterDemo():
    Name = input("Enter Name: ")
    Age = float(input("Enter Age: "))
    print(f"{Name}\n{Age}")
    print(f"{Name}\"{Age}")
    print(f"{Name}\'{Age}")
    print(f"{Name}\\{Age}")
def TextAnalyzer():
    Sentence = input("Enter A Sentence: ")
    if Sentence:
        print(f"first and last character:{Sentence[0]},{Sentence[-1]}")
    else:
        print("no sentence is enter")
    print(f"Count length:{len(Sentence)}")
    Word = input("Enter Search for a specific word: ")
    print(f"Search for a specific word:{Word in Sentence}")
    Replace_word = input("Enter Replace Word: ")
    New_Word = input("Enter New Word: ")
    print(f"Replace a word:{Sentence.replace(Replace_word,New_Word)}")
    print(f"Trim spaces:{Sentence.strip()}")
    print(f"Convert to upper and lower case:{Sentence.upper()},{Sentence.lower()}")
def SentenceTools():
    Sentence = input("Enter Sentence: ")
    Word = input("Enter Count the occurrences of a word: ")
    print(f"Count the occurrences of a word:{Sentence.count(Word)}")
    print(f"LowerCase:{Sentence.lower()}")
    print(f"UpperCase:{Sentence.upper()}")
    print(f"TitleCase:{Sentence.title()}")
    print(f"Capitalize:{Sentence.capitalize()}")
    Start_Text = input("Enter A Word To Check Start With: ")
    End_Text = input("Enter A Word To Check End With: ")
    print(f"Check Sentence starts with a given text:{Sentence.startswith(Start_Text)}")
    print(f"Check Sentence ends with a given text:{Sentence.endswith(End_Text)}")
def ViewStudentInfoDaysOfTheWeek():
    global name,age,percentage
    if name is None:
        print("Please Enter option 1")

    print(f"Name Is:{name}")
    print(f"Age Is:{age}")
    print(f"Percentage Is:{percentage}")
    Days = ["Mon","tue","wed","thu","fri","sat"]
    print(f"Display the first day:{Days[0]}")
    print(f"Display the fifth day:{Days[4]}")
    print(f"Display the last day:{Days[-1]}")
    print(f"Display total number of days:{len(Days)}")
    try:
        print(Days[8])
    except IndexError:
        print("index out-of-range errors ")

Fruits = ["Apple","Mango","Papaya","banana"]
Extra_Fruits = ["Watermelon","orange"]
def ViewFruits():
    print(f"all fruits in the fruit basket.:{Fruits}")

def AddFruit():
    AddF = input("Enter a new fruit to the basket.: ")
    Fruits.append(AddF)
    print(Fruits)
def InsertFruit():
    Insert = input("Enter Fruits Name: ")
    Index = int(input("Enter Index: "))
    if Index > len(Fruits):
        print("Error Index Is out of range")
    else:
        Fruits.insert(Index,Insert)
        print(Fruits)

def CombineWithExtraFruits():
    print(Fruits + Extra_Fruits)
def RepeatFruits():
    Numbers = int(input("Repeat the fruit basket n times based on user input.: "))
    print(Fruits * Numbers)
def Main():
    while True:
        print("""
--- STUDENT UTILITIES ---
1. Student Marks Report
2. Temperature Conversion
3. Simple Interest Calculator
4. Math Operations
5. String Operations
6. Escape Character Demo
7. Text Analyzer
8. Sentence Tools
9. View Student Info & Week Days

--- FRUIT BASKET MANAGER ---
10. View Fruits
11. Add Fruit
12. Insert Fruit
13. Combine With Extra Fruits
14. Repeat Fruits

15. Exit Program
""")
        Choice = int(input("Enter Choice From 1 to 15: "))
        if Choice == 1:
            StudentMarksReport()
        elif Choice == 2:
            TemperatureConversion()
        elif Choice == 3:
            SimpleInterestCalculator()
        elif Choice == 4:
            MathOperations()
        elif Choice == 5:
            StringOperations()
        elif Choice == 6:
            EscapeCharacterDemo()
        elif Choice == 7:
            TextAnalyzer()
        elif Choice == 8:
            SentenceTools()
        elif Choice == 9:
            ViewStudentInfoDaysOfTheWeek()
        elif Choice == 10:
            ViewFruits()
        elif Choice == 11:
            AddFruit()
        elif Choice == 12:
            InsertFruit()
        elif Choice == 13:
            CombineWithExtraFruits()
        elif Choice == 14:
            RepeatFruits()
        elif Choice == 15:
            print("Exit Program")
            break
        else:
            print("Error Choice")

Main()





