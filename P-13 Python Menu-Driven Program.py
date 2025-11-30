def Main():
    while True:
        def StudentMarksReport():
            StudentName = input("Enter Student Name: ")
            Age = float(input("Enter Age: "))
            ProgrammingLanguageLearned = input("Enter Programming Language Learned: ")
            StudyHours = float(input("Enter Study Hours per Day: "))
            MarksOfSubject1 = float(input("Enter Marks of Subjects1: "))
            MarksOfSubject2 = float(input("Enter Marks of Subjects2: "))
            MarksOfSubject3 = float(input("Enter Marks of Subjects3: "))
            TotalMarks = MarksOfSubject1 + MarksOfSubject2 + MarksOfSubject3
            Percentage = TotalMarks / 3
            print("="*7, "Student Marks Report","="*7)
            print(f"Student Name Is:{StudentName}.Age Of Student Is:{Age}")
            print(f"ProgrammingLanguageLearned Is:{ProgrammingLanguageLearned}")
            print(f"Study Hours Per Day:{StudyHours}")
            print(f"Marks Of Subject1,Subject2,Subject3 Is:{MarksOfSubject1},{MarksOfSubject2},{MarksOfSubject3}")
            print(f"Total Marks Is:{TotalMarks}")
            if Percentage >= 90:
                print("Grade:A+")
            elif Percentage >= 75:
                print("Grade:A")
            elif Percentage >= 60:
                print("Grade:B")
            elif Percentage < 60:
                print("Grade:C")
        def TemperatureConversion():
            print("1.Celsius to Fahrenheit")
            print("2.Fahrenheit to Celsius")
            Choice = int(input("Enter Choice From 1 to 2: "))
            def CelsiusToFahrenheit():
                Celsius = float(input("Enter Temperature In Celsius: "))
                Fahrenheit = (Celsius * 9 /5 ) + 32
                print(f"Temperature Celsius To Fahrenheit:{Fahrenheit}")
            def FahrenheitToCelsius():
                Fahrenheit = float(input("Enter Temperature In Fahrenheit: "))
                Celsius = (Fahrenheit - 32) * 5 / 9
                print(f"Temperature Fahrenheit To Celsius:{Celsius}")
            if Choice == 1:
                CelsiusToFahrenheit()
            elif Choice == 2:
                FahrenheitToCelsius()
            else:
                print("ERROR Enter Choice From 1 To 2")
        def SimpleInterestCalculator():
            Principal = float(input("Enter Principal Amount: "))
            RateOfInterest = float(input("Enter Rate Of Interest: "))
            Time = float(input("Enter Time In Years: "))
            SimpleInterest = (Principal * RateOfInterest * Time) / 100
            print(f"Simple Interest Is:{SimpleInterest}")
        def MathOperations():
            Numbers = input("Enter input multiple numbers separated by spaces: ").split()
            nums = []
            for i in Numbers:
                num = float(i)
                nums.append(num)
            print(f"Maximum And Minimum Value Is:{max(nums)},{min(nums)}\n")
            Number = float(input("Enter one number For Absolute Value: "))
            print(f"The absolute value of a number:{abs(Number)}\n")
            Base = float(input("Enter Base Value: "))
            Exponent = float(input("Enter Exponent Value: "))
            print(f"The result of Base:{Base} raised to Exponent:{Exponent} Is:{pow(Base,Exponent)}")
        def StringOperations():
            String = "Hello World"
            print(f"Length of the string Is:{len(String)}")
            print(f"First character Is:{String[0]}")
            print(f"Last character Is:{String[-1]}")
            print(f"Data type of the string:{type(String)}")
        def EscapeCharacterDemonstration():
            Name = input("Enter Name:" )
            Age = float(input("Enter Age: "))
            print(f"Name:{Name}\tAge:{Age}")
            print(f"Name:\"{Name}\"Age:{Age}")
            print(f'Name:\'{Name}\'Age:{Age}')
            print(f'Name:\\\\{Name}\\\\Age:{Age}')
        def TextAnalyzer():
            Sentence = input("Enter A Sentence: ")
            print(f"the first character:{Sentence[0]}")
            print(f"the last character:{Sentence[-1]}")
            print(f"the length of the sentence:{len(Sentence)}")
            Word = input("Enter Word To Check In Sentence: ")
            print(Word in Sentence)
            Word = input("Enter Word To Replace: ")
            NewWord = input("Enter New Word: ")
            print(Sentence.replace(Word,NewWord))
            print(Sentence.strip())
            print(Sentence.upper())
            print(Sentence.lower())
        Choice = int(input("Enter Choice From 1 to 8: "))
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
            TextAnalyzer()
        elif Choice == 8:
            print("You Exit The Loop")
            break
        else:
            print("Error Enter Choice From 1 to 8")











