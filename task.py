#Task 1: Calculate Simple Interest
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

si = (p * r * t) / 100
print("Simple Interest =", si)


#Task 2: Print numbers from 1 to 5
for i in range(1, 6):
    print(i)
    
    
#Task 3: Find maximum of 2 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Maximum number is", a)
else:
    print("Maximum number is", b)
    
#Task 4: Find length of a string
text = input("Enter a string: ")
print("Length of string =", len(text))

#Task 5: Print a welcome message
print("Welcome to Python Programming!")

#Task 6: Print first character of a string
text = input("Enter a string: ")
print("First character is:", text[0])

#Task 7: Print last character of a string
text = input("Enter a string: ")
print("Last character is:", text[-1])

#Task 8: Check positive or negative number
num = int(input("Enter a number: "))

if num >= 0:
    print("Number is Positive")
else:
    print("Number is Negative")


#Task 9: Add 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

sum = a + b + c
print("Sum =", sum)

#Task 10: Take input from user and make a task

num = int(input("Enter a number: "))
print("Square =", num * num)









