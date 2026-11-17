print('Hello, Siddhu!')

#Ask the user for their name and print Hello, <name>!
name = input("Enter your name: ")
print("Hello,", name + "!")

#Take two numbers and print their sum, difference, and product.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("sum:", a+b)
print("Difference:", a-b)
print("product:", a*b)

#Check whether a number is even or odd.
n = int(input("Enter a number: "))
if n%2 == 0:
    print("Even")
else:
    print("odd")

#Print the multiplication table of any number.
num = int(input("Enter number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

#Sum all numbers from 1 to 100 using a loop.
total = 0
for i in range(1,101):
    total = total + i
print("sum=",total)

#Take marks as input and print a grade (A/B/C/Fail).
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Fail")

#Print the largest of three numbers.
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x >= y and x >= z:
    print("Largest number is:",x)
elif y >= x and y >= z:
    print("Largest number is:",y)
else:
    print("Largest number is:",z)
