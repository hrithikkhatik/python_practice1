def Main():
    while True:
        def StudentMarksReport():
            Name = str(input("Kindly Enter Name: "))
            Age = float(input("Kindly Enter Age: "))
            ProgrammingLanguage = str(input("Kindly Enter Programming Language: "))
            StudyHours = float(input("Kindly Enter Study Hours: "))
            MarksOfSubject1 = float(input("Kindly Enter Marks of Subject 1: "))
            MarksOfSubject2 = float(input("Kindly Enter Marks of Subject 2: "))
            MarksOfSubject3 = float(input("Kindly Enter Marks of Subject 3: "))
            TotalMarks = (MarksOfSubject1 + MarksOfSubject2 + MarksOfSubject3)
            Percentage = TotalMarks / 3
            print(f"Student Name Is:{Name}")
            print(f"Student Age Is:{Age}")
            print(f"Programming Language Learn:{ProgrammingLanguage}")
            print(f"Study Hours:{StudyHours}")
            print(f"Total Marks Is:{TotalMarks}")
            print(f"Percentage Is:{Percentage}")
            if Percentage >= 90:
                print("Grade Is:A+")
            elif Percentage >= 75:
                print("Grade Is:A")
            elif Percentage >= 60:
                print("Grade Is:B")
            elif Percentage < 60:
                print("Grade Is:C")

        def TemperatureConversion():
            print("Choice: 1 for Celsius → Fahrenheit, 2 for Fahrenheit → Celsius")
            Choice = int(input("Choice: 1 for Celsius → Fahrenheit, 2 for Fahrenheit → Celsius"))
            def CelsiusFahrenheit():
                Celsius = float(input("Enter Temperature In Celsius: "))
                Fahrenheit = (Celsius * 9 / 5) + 32
                print(f"Temperature Celsius To Fahrenheit:{Fahrenheit}")
            def FahrenheitCelsius():
                Fahrenheit = float(input("Enter Temperature In Fahrenheit: "))
                Celsius = (Fahrenheit - 32) * 5 / 9
                print(f"Temperature Fahrenheit To Celsius:{Celsius}")
            if Choice == 1:
                CelsiusFahrenheit()
            elif Choice == 2:
                FahrenheitCelsius()
            else:
                print("Error Enter 1 to 2.")
        def SimpleInterestCalculator():
            Principal = float(input("Enter Principal Amount: "))
            RateOfInterest = float(input("Enter Rate Of Interest: "))
            TimeInYears = float(input("Enter Time In Years: "))
            SimpleInterest = (Principal * RateOfInterest * TimeInYears) / 100
            print(f"Simple Interest is:{float(SimpleInterest)}")
        def MathOperations():
            Numbers = input("List of numbers (space-separated): ").split()
            Nums = []
            for i in Numbers:
                Num = float(i)
                Nums.append(Num)
            print(f"Maximum And Minimum Value Is:{max(Nums)},{min(Nums)}")
            number = float(input("Enter Number to find absolute value: "))
            print(f"absolute value Is:{abs(number)}")

            Base = float(input("Enter Base Value: "))
            Exponent = float(input("Enter Exponent Value: "))
            print(f"Result of number raised to the given exponent:{pow(Base,Exponent)}")

        def StringOperations():
            String = "Hello World"
            print(f"Length Of String Is:{len(String)}")
            print(f"First And Last Character Of String Is:{String[0]},{String[-1]}")
            print(f"Data type of the string Is:{type(String)}")

        def EscapeCharacterDemo():
            Name = input("Enter Name: ")
            Age = float(input("Enter Age: "))
            print(f"{Name}\n{Age}")
            print(f"\"{Name}\"\n{Age}")
            print(f'\'{Name}\'\n{Age}')
            print(f"{Name}\\{Age}")
            print(f"{Name}\\\\{Age}")

        def TextAnalyzer():
            Sentence = str(input("Enter A Sentence: "))
            SubString = str(input("Enter Word to check existence In Sentence: "))
            Replace = input("Enter Word to replace: ")
            New_Word = input("Enter new word: ")
            print(f"First and last character:{Sentence[0]},{Sentence[-1]}")
            print(f"Length Of Sentence:{len(Sentence)}")
            print(f"Check if a {SubString} exists:{SubString in Sentence}")
            print(f"Replace a {Replace} with {New_Word}:{Sentence.replace(Replace,New_Word)}")
            print(f"Strip extra spaces:{Sentence.strip()}")
            print(f"convert to upper and lower case:{Sentence.upper()},{Sentence.lower()}")

        def SentenceTools():
            Sentence = str(input("Enter A Sentence: "))
            SubString = str(input("Enter Word to check existence In Sentence: "))
            Start_Text = input("Enter Start Text: ")
            End_Text = input("Enter End Text: ")
            print(f"Count occurrences of substring:{Sentence.count(SubString)}")
            print(f"Convert sentence to lowercase:{Sentence.lower()}")
            print(f"Convert sentence to Uppercase:{Sentence.upper()}")
            print(f"Convert sentence to Titlecase:{Sentence.title()}")
            print(f"Convert sentence to capitalize:{Sentence.capitalize()}")
            print(f"sentence starts:{Start_Text} or ends:{End_Text} with given text:{Sentence.startswith(Start_Text)},{Sentence.endswith(End_Text)}")

        Choice = int(input("Menu choice (integer 1-9): "))
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
            print("You Successfully Exit Program.")
            break
        else:
            print("Error Enter 1 to 9")

Main()







