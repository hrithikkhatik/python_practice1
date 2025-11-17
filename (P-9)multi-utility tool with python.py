try:
    StudentName = input("Enter Student Name: ")
    Age = float(input("Enter Student age: "))
    ProgrammingLanguageLearned = input("Enter Programming Language You Learn: ")
    StudyHoursperDay = float(input("Enter Study Hours per Day: "))
    Marksofsubject1 = float(input("Enter Marks Of Subject1: "))
    Marksofsubject2 = float(input("Enter Marks Of Subject2: "))
    Marksofsubject3 = float(input("Enter Marks Of Subject3: "))
    TotalMarks = Marksofsubject1 + Marksofsubject2 + Marksofsubject3
    Percentage = TotalMarks / 3
    print(f"Student Name Is:{StudentName}")
    print(f"Student Age Is:{Age}")
    print(f"Programming Language Learned:{ProgrammingLanguageLearned}")
    print(f"Study Hours per Day:{StudyHoursperDay}")
    print(f"MarksOfSubject1:{Marksofsubject1},MarksofSubject2:{Marksofsubject2},MarksOfSubject3:{Marksofsubject3}")
    print(f"Total Marks Is:{TotalMarks}")
    print(f"Percentage Is:{Percentage}")
    if Percentage >= 90:
        print("Excellent! Keep it up!")
    elif Percentage >= 75:
        print("Very Good!")
    elif Percentage >= 60:
        print("Good Job!")
    elif Percentage < 60:
        print("Needs Improvement.")
except ValueError:
    print("Kindly Enter A Valid input")
def Main():
    while True:
        try:
            def StudentMarksReport():
                StudentName = input("Enter Student Name: ")
                Age = float(input("Enter Student age: "))
                ProgrammingLanguageLearned = input("Enter Programming Language You Learn: ")
                StudyHoursperDay = float(input("Enter Study Hours per Day: "))
                Marksofsubject1 = float(input("Enter Marks Of Subject1: "))
                Marksofsubject2 = float(input("Enter Marks Of Subject2: "))
                Marksofsubject3 = float(input("Enter Marks Of Subject3: "))
                TotalMarks = Marksofsubject1 + Marksofsubject2 + Marksofsubject3
                Percentage = TotalMarks / 3
                print(f"Student Name Is:{StudentName}")
                print(f"Student Age Is:{Age}")
                print(f"Programming Language Learned:{ProgrammingLanguageLearned}")
                print(f"Study Hours per Day:{StudyHoursperDay}")
                print(
                    f"MarksOfSubject1:{Marksofsubject1},MarksofSubject2:{Marksofsubject2},MarksOfSubject3:{Marksofsubject3}")
                print(f"Total Marks Is:{TotalMarks}")
                print(f"Percentage Is:{Percentage}")
                if Percentage >= 90:
                    print("Grade:A+")
                elif Percentage >= 75:
                    print("Grade:A")
                elif Percentage >= 60:
                    print("Grade:B")
                elif Percentage < 60:
                    print("Grade:C")
        except ValueError:
            print("Kindly Enter A Valid input")
        def TemperatureConversion():
            try:
                Celsius = float(input("Enter Temperature in Celsius: "))
                Fahrenheit = (Celsius * 9/5) + 32
                print(f"Tempreature Converted Celsius To Fahrenheit:{Fahrenheit}")
                Fahrenheit = float(input("Enter Temperature in Fahrenheit: "))
                Celsius = (Fahrenheit - 32) * 5/9
                print(f"Temperature Converted Fahrenheit To Celsius:{Celsius}")
            except ValueError:
                print("Kindly Enter A Valid input")
        def SimpleInterestCalculator():
            try:
                Principal = float(input("Enter Principal Amount: "))
                RateofInterest = float(input("Enter Rate Of Interest: "))
                Time = float(input("Enter Time (T in years): "))
                SimpleInterest =  (Principal * RateofInterest * Time) / 100
                print(f"Simple Interest is:{SimpleInterest}")
            except ValueError:
                print("Kindly Enter A Valid input")
        def MathOperations():
            try:
                Numbers = input("Enter Number With Sepreated: ").split()
                nums = []
                for i in Numbers:
                    num = float(i)
                    nums.append(num)
                print(f"Maximum Value is:{max(nums)},Minimum Value Is:{min(nums)}")
                Numbers = float(input("Enter any single number: "))
                print(f"Absolute Value Is:{abs(Numbers)}")
                Base = float(input("Enter Base Value: "))
                Exponent = float(input("Enter Exponent Value: "))
                print(f"power (Base^Exponent) is:{pow(Base,Exponent)}")
            except ValueError:
                print("Kindly Enter A Valid input")
        def StringOperations():
            try:
                String = "Hello World"
                print(f"Length Of String Is:{len(String)}")
                print(f"First Character Is:{String[0]},Last Character Of String Is:{String[-1]}")
                print(f"Slice of String:{String[0:2]}")
                print(type(String))
                print(type(String[0:2:2]))
                print(type(String[0:5:3]))
                print(type(String[0:8:4]))
            except ValueError:
                print("Kindly Enter A Valid input")
        try:
            Choice = int(input("Enter Your Choice: "))
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
                print("You Successfully Terminate the program")
                break
        except ValueError:
            print("Kindly Enter A Valid input")
Main()
