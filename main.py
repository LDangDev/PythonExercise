import math;
import random
# 1. First program and deployment of version control
# Ex 1
print(f"Hello, Loc!")
# Ex 2

# 2. Variables and interactive programs
# Ex 1
name = input("Enter your name: ")
print(f"Hello {name}!")

# Ex 2
pi = math.pi
radius = float(input("Enter radius: "))
print(f"Area of the circle is: {pi * radius:.5f}")

# Ex 3
length = int(input("Enter length: "))
width = int(input("Enter width: "))
perimeter = length * 2 + width * 2
area = length * width
print(f"Perimeter is: {perimeter}")
print(f"Area is: {area}")

# Ex 4
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
input3 = int(input("Enter third number: "))
sum = (input1 + input2 + input3)
avg =  float((input1 + input2 + input3) / 3)
product = input1 * input2 * input3
print(f"Sum is: {sum}")
print(f"Product is: {product}")
print(f"Average is: {avg:.2f}")

# Ex 5
talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))
total_in_grams = ((talents * 20)* 32)* 13.3 + pounds * 32 * 13.3 + lots * 13.3
kilo = math.floor((total_in_grams) / 1000)
grams = total_in_grams % 1000
print(f"{total_in_grams}")
print(f"The weight in modern units:\n")
print(f"{kilo} kilograms and {grams:.2f}")

# Ex 6
n = 0
random_1 = ''
random_2 = ''
while n < 3:
    random_1 += str(random.randint(0, 9))
    n += 1
n = 0
while n < 4:
    random_2 += str(random.randint(1, 6))
    n += 1
print(f"A 3-digit code random: {random_1}")
print(f"A 4-digit code random: {random_2}")

# 3. Conditional structures (if)
# Ex 1
input = float(input("Enter length of zander(in cm): "))
if(input < 42):
    print(f"Release the fish back into lake. The size must be at lease 42 cm to catch")
else:
    print(f"Congratulation! you are not hungry any more")
# Ex 2
input = input("Enter a cabin class: ")
if(input == "LUX"):
    print(f"upper-deck cabin with a balcony.")
elif(input == "A"):
    print(f"above the car deck, equipped with a window.")
elif(input == "B"):
    print(f"windowless cabin above the car deck.")
elif(input == "C"):
    print(f"windowless cabin below the car deck.")
else:
    print(f"Invalid cabin class")
# Ex 3
gender = input("Enter your gender: ")
if(gender == "males"):
    hemoglobin = float(input("Enter hemoglobin value: "))
    if(hemoglobin < 134):
        print(f"low")
    elif(hemoglobin > 167):
        print(f"high")
    else:
        print(f"normal")
elif(gender == "female"):
    hemoglobin = float(input("Enter hemoglobin value: "))
    if(hemoglobin < 117):
        print(f"low")
    elif(hemoglobin > 155):
        print(f"high")
    else:
        print(f"normal")
else:
    print(f"please enter a valid gender males or females")

# Ex 4
year = int(input("Enter a year: "))
year = int(input("Enter a year: "))
if((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)):
    print(f"Leap year")
else:
    print(f"not leap year")

# 4. While loops (while)
# Ex 1
n = 1
while(n <= 1000):
    print(f"{n}")
    n += 1
# Ex 2
while True:
    inches = float(input("Enter inches: "))
    if(inches >= 0):
        result = inches * 2.54
        print(f"Converted to cm: {result}")
    else:
        break
# Ex 3
numbers = []
while True:
    user_input = input("Enter a number: ")
    if(user_input == ''):
        break
    else:
        number = int(user_input) 
        numbers.append(number)

minNum = min(numbers)
maxNum = max(numbers)
print(f"Min number: {minNum}")
print(f"Max number: {maxNum}")

# Ex 4
random_num = random.randint(1, 10)
while True:
    guess = int(input("Enter your guess: "))
    if(guess == random_num):
        print(f"Correct!")
        break
    elif(guess < random_num):
        print(f"Too low")
    else:
        print(f"Too high")