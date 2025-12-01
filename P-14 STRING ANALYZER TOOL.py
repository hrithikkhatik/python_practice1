Sentence = input("Enter A full sentence: ")
SubString = input("Enter A substring they want to count inside the sentence: ")
Count = Sentence.count(SubString)
print(f"Occurrences of '{SubString}' In Sentence = {Count}")
print(f"Sentence In LowerCase:{Sentence.lower()}")
print(f"Sentence In UpperCase:{Sentence.upper()}")
print(f"Sentence In TitleCase:{Sentence.title()}")
print(f"Sentence In Capitalize:{Sentence.capitalize()}")
Start_With = input("Enter Text to check whether the sentence starts with it: ")
End_With = input("Enter Text to check whether the sentence ends with it: ")
print(f"Starts with '<{Start_With}'? : {Sentence.startswith(Start_With)}")
print(f"Ends with '<{End_With}'? : {Sentence.endswith(End_With)}")
print("Analysis Completed Successfully!")







