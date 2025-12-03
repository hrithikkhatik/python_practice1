name = None
age = None
percentage = None
def StudentMarksReport():
    global name , age , percentage
    StudentName = input("Enter Student Name: ")
    Age = float(input("Enter Age: "))
    Programming = input("Enter Programming language being learned: ")
    Study = float(input("Enter Study hours per day: "))
    Marks1 = float(input("Enter Marks in subject1: "))
    Marks2 = float(input("Enter Marks in subject2: "))
    Marks3 = float(input("Enter Marks in subject3: "))
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
    name = StudentName
    age = Age
    percentage = Percentage
def TemperatureConversion():
    print("1.Celsius to Fahrenheit")
    print("2.Fahrenheit to Celsius")
    def CelsiusToFahrenheit():
        Celsius = float(input("Enter Temperature In Celsius: "))
        Fahrenheit = (Celsius * 9 / 5) + 32
        print(f"Temperature Celsius To Fahrenheit:{Fahrenheit}")
    def FahrenheitToCelsius():
        Fahrenheit = float(input("Enter Temperature In Fahrenheit: "))
        Celsius = (Fahrenheit - 32) * 5 / 9
        print(f"Temperature Fahrenheit To Celsius:{Celsius}")
    Choice = int(input("Enter Choice From 1 to 2: "))
    if Choice == 1:
        CelsiusToFahrenheit()
    elif Choice == 2:
        FahrenheitToCelsius()
    else:
        print("Invalid Option")
def SimpleInterestCalculator():
    Principal = float(input("Enter Principal Amount: "))
    Rate = float(input("Enter Rate Of Interest: "))
    Time = float(input("Enter Time in years: "))
    SimpleInterest = (Principal * Rate * Time) / 100
    print(f"Simple Interest:{SimpleInterest}")
def MathOperations():
    Numbers = input("Enter List of numbers (space-separated):").split()
    Nums = []
    for i in Numbers:
        num = float(i)
        Nums.append(num)
    number = float(input("Enter A number to find absolute value: "))
    Base = float(input("Enter Base for power calculation: "))
    Exponent = float(input("Enter exponent for power calculation: "))
    print(f"Maximum and Minimum Value Is:{max(Nums)},{min(Nums)}")
    print(f"Absolute value of the number:{abs(number)}")
    print(f"Base raised to the exponent:{pow(Base,Exponent)}")
def StringOperations():
    String = "Hello World"
    print(f"Length of the string:{len(String)}")
    print(f"First and last character:{String[0]},{String[-1]}")
    print(f"Data type of the string:{type(String)}")
def EscapeCharacterDemo():
    Name = input("Enter Name: ")
    Age = input("Enter Age: ")
    print(f"{Name}\n{Age}")
    print(f"{Name}\"{Age}")
    print(f"{Name}\'{Age}")
    print(f"{Name}\\{Age}")
def TextAnalyzer():
    Sentence = input("Enter Sentence: ")
    Word = input("Enter A word to check existence: ")
    Word_Replace = input("Enter A word to replace: ")
    Word_New = input("Enter its replacement: ")
    print(f"First and last character of the sentence:{Sentence[0]},{Sentence[-1]}")
    print(f"Length of the sentence:{len(Sentence)}")
    print(f"Check if the word exists:{Word in Sentence}")
    print(f"Replace a word:{Sentence.replace(Word_Replace,Word_New)}")
    print(f"Remove extra spaces:{Sentence.strip()}")
    print(f"Convert sentence to uppercase and lowercase:{Sentence.upper()}\n{Sentence.lower()}")
def SentenceTools():
    Sentence = input("Enter Sentence: ")
    Word = input("Enter A word to count: ")
    StartText = input("Enter Start Text: ")
    EndText = input("Enter End Text: ")
    print(f"Count of occurrences of the word:{Sentence.count(Word)}")
    print(f"Sentence in lowercase, uppercase, title case, and capitalized:{Sentence.lower()}\n,{Sentence.upper()},\n{Sentence.title()},\n{Sentence.capitalize()}")
    print(f"Check if sentence starts with start text or ends with end text:{Sentence.startswith(StartText)},\n{Sentence.endswith(EndText)}")
def ViewStudentInfoDaysOfTheWeek():
    global name , age , percentage
    if name is None:
        print("Kindly enter option 1 first")
        return
    print(f"Name:{name},\nAge:{age},\n{percentage}")
    DaysOfWeek = ["mon","tue","wed","thu","fri","sat","sun"]
    print(f"Days of the week (first, fifth, last):{DaysOfWeek[0]},{DaysOfWeek[4]},{DaysOfWeek[-1]}")
    print(f"Total number of days:{len(DaysOfWeek)}")
    try:
        print(f"{DaysOfWeek[8]}")
    except IndexError:
        print("index out of range")
def Main():
    while True:
        Choice = int(input("Enter Choice 1 to 10: "))
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
            print("Stop the program")
            break
        else:
            print("invalid option")

