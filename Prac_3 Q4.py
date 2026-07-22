#Question 4

age= int(input("Enter your age: "))
nationality=input("Enter your nationality: ")

if age>=18:
    if nationality.lower() == "indian":
        print("Eligible to Vote.")
    else:
        print("Not eligible to Vote")
else:
    print("Not Eligible to Vote")
