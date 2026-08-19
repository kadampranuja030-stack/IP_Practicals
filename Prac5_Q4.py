n=int(input("Enter the number of elements: "))
numbers=[]

for i in range(n):
    value=int(input("Enter element: "))
    numbers.append(value)

search=int(input("Enter the number to search:"))

found=False

for i in range(len(numbers)):
    if numbers[i] == search:
        print (search, "found at Position",i)
        found=True
        break

if found == False:
    print(search, "not found in the list.")
