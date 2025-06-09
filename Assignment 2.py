# Task 1:

Num = float(input("Enter the number: "))
if Num % 2 == 0:
    print("Given number",Num,"is Even")
else:
    print("Given number",Num,"is Odd")


# Task 2:
    

Num1 = int(input("Enter the First number: "))
Num2 = int(input("Enter the Second number: "))
total = 0
for i in range (Num1, Num2 + 1):
    total += i
print("Total Sum of",Num1,"and",Num2,"is:",total)
