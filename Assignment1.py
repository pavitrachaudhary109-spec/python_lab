#1. Write a Python program to display a welcome message.
print("Welcome to Python programming!")
#2. Write a Python program to print an address using \t for tab spaces and \n for new lines.
print("Rajesh Kumar\nFlat No. 101, Sunshine Apartments\nMG Road, Sector 15\nRajkot,\nPincode: 360004\nIndia.")

#3. Write a Python program to perform four basic mathematical operations (addition, subtraction, multiplication, and division) using the values 150 and 120.50.
a = 150
b = 120.50

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

#4. Write a program that calculates the area of a circle given its radius.
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius

print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")

#5. Write a program that calculates the simple interest using the formula.
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time in years: "))

simple_interest = (P * R * T) / 100
print(f"Simple Interest: {simple_interest}")

#6. Write a program to calculate the perimeter of a rectangle.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = 2 * (length + width)
print(f"Perimeter of the rectangle: {perimeter}")

#7. Write a program that calculates the area and perimeter of a rectangle using the formulas.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")


#8. Write a program that calculates the perimeter of a triangle.
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

perimeter_triangle = a + b + c
print(f"Perimeter of the triangle: {perimeter_triangle}")

#9. Write a program that calculates the area and perimeter of a square using the formulas.
side = float(input("Enter the side length of the square: "))

area_square = side ** 2
perimeter_square = 4 * side

print(f"Area of the square: {area_square}")
print(f"Perimeter of the square: {perimeter_square}")

#10. Write a program that calculates the perimeter of a square.
side = float(input("Enter the side length of the square: "))

perimeter_square = 4 * side
print(f"Perimeter of the square: {perimeter_square}")