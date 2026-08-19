#Q5
n=int(input("Enter a Number: "))

for i in range (2,101):
    if n% i == 0:
        print("First number divisible by", n, "is",i)
        break
