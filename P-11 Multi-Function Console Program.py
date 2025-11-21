def Main():
    while True:
        def StudentMarksReport():
            StudentName = input("Enter Student Name: ")
            Age = float(input("Enter Age: "))
            ProgrammingLanguagelearned = input("Enter Programming Language learned: ")
            Studyhoursperday = float(input("Enter Study hours per day: "))
            Marksofsubjects1 = float(input("Enter Marks Of Subject 1: "))
            Marksofsubjects2 = float(input("Enter Marks Of Subject 2: "))
            Marksofsubjects3 = float(input("Enter Marks Of Subject 3: "))
            TotalMarks = Marksofsubjects1 + Marksofsubjects2 + Marksofsubjects3
            Percentage = TotalMarks / 3
            print("-"*5,"STUDENT REPORT","-"*5)
            print(f"Name:{StudentName}")
            print(f"Age:{Age}")
            print(f"Language:{ProgrammingLanguagelearned}")
            print(f"Study Hours:{Studyhoursperday}")
            print(f"Total Marks:{TotalMarks}")
            print(f"Percentage:{Percentage}")
            if Percentage >= 90:
                print("Grade:A+")
            elif Percentage >= 75:
                print("Grade:A")
            elif Percentage >= 60:
                print("Grade:B")
            elif Percentage < 60:
                print("Grade:C")
        def TemperatureConversion():
            def CelsiusToFahrenheit():
                Celsius = float(input("Enter Temperature in Celsius: "))
                Fahrenheit = (Celsius * 9/5) + 32
                print(f"Tempreature Celsius To Fahrenheit:{Fahrenheit}")
            def FahrenheitToCelsius():
                Fahrenheit = float(input("Enter Temperature in Fahrenheit: "))
                Celsius = (Fahrenheit - 32) * 5/9
                print(f"Tempreature Fahrenheit To Celsius:{Celsius}")
            Choice = float(input("Enter Your Choice: "))
            if Choice == 1:
                CelsiusToFahrenheit()
            elif Choice == 2:
                FahrenheitToCelsius()
            else:
                print("Enter Option From 1 to 2")
        def SimpleInterestCalculator():
            PrincipalAmount = float(input("Enter Principal Amount: "))
            RateofInterest = float(input("Enter Rate Of Interest: "))
            TimeinYears = float(input("Enter Time In Years: "))
            SimpleInterest = (PrincipalAmount * RateofInterest * TimeinYears) / 100
            print(f"Simple Interest Is:{SimpleInterest}")
        def MathOperations():
            Numbers = input("Enter A list of numbers separated by spaces: ").split()
            Num = [float(i) for i in Numbers]
            print(f"Maximum Value Is:{max(Num)} and Minimum Value Is:{max(Num)}")
            Number = float(input("ENter Number For Absolute Value: "))
            print(f"Absolute Value Is:{Number}")
            Base = float(input("Enter Base Value: "))
            Exponent = float(input("Enter Exponent Value: "))
            print(f"base^exponent:{pow(Base,Exponent)}")
        def StringOperations():
            String = "Hello World"
            print(f"Length of the string:{len(String)}")
            print(f"First and last characters:{String[0]} and {String[-1]}")
            A = String[0:2]
            print(type(String))
            print(type(A))
        def EscapeCharacterDemonstration():
            Name = input("Enter Name: ")
            Age = float(input("Enter Age: "))
            print("Hello\tUser")
            print(f"Your name is \n\"{Name}\n\"")
            print(f"You\n\'re {Age} years old")
            print("Path example: C:\n\nUsers\n\nAli")
        Choice = float(input("Enter Your Choice: "))
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
            EscapeCharacterDemonstration()
        elif Choice == 7:
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Enter Choice From 1 to 7")
Main()






