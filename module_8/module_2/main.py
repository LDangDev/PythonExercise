import math
import random

# 2. Variables and interactive programs
# Ex 1
name = input("Enter your name: ")
print(f"Hello {name}!")

# Ex 2
pi = math.pi
radius = float(input("Enter radius: "))
print(f"Area of the circle is: {pi * radius:.5f}")

# Ex 3
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = length * 2 + width * 2
area = length * width
print(f"Perimeter is: {perimeter:.2f}")
print(f"Area is: {area:.2f}")

# Ex 4
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
input3 = int(input("Enter third number: "))
sum = input1 + input2 + input3
avg = (input1 + input2 + input3) / 3
product = input1 * input2 * input3
print(f"Sum is: {sum}")
print(f"Product is: {product}")
print(f"Average is: {avg:.2f}")

# Ex 5
talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))
total_in_grams = talents * 20 * 32 * 13.3 + pounds * 32 * 13.3 + lots * 13.3
kilo = math.floor(total_in_grams / 1000)
grams = total_in_grams % 1000
print(f"The weight in modern units:\n{kilo} kilograms and {grams:.2f}")

# Ex 6
n = 0
random_1 = ""
random_2 = ""
while n < 3:
    random_1 += str(random.randint(0, 9))
    n += 1
n = 0
while n < 4:
    random_2 += str(random.randint(1, 6))
    n += 1
print(f"A 3-digit code random: {random_1}")
print(f"A 4-digit code random: {random_2}")