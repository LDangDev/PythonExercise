import math
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
sum = input1 + input2 + input3
avg = float((input1 + input2 + input3) / 3)
product = input1 * input2 * input3
print(f"Sum is: {sum}")
print(f"Product is: {product}")
print(f"Average is: {avg:.2f}")

# Ex 5
talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))
total_in_grams = ((talents * 20) * 32) * 13.3 + pounds * 32 * 13.3 + lots * 13.3
kilo = math.floor((total_in_grams) / 1000)
grams = total_in_grams % 1000
print(f"{total_in_grams}")
print(f"The weight in modern units:\n")
print(f"{kilo} kilograms and {grams:.2f}")

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

# 3. Conditional structures (if)
# Ex 1
input = float(input("Enter length of zander(in cm): "))
if input < 42:
    print(f"Release the fish back into lake. The size must be at lease 42 cm to catch")
else:
    print(f"Congratulation! you are not hungry any more")
# Ex 2
input = input("Enter a cabin class: ")
if input == "LUX":
    print(f"upper-deck cabin with a balcony.")
elif input == "A":
    print(f"above  the car deck, equipped with a window.")
elif input == "B":
    print(f"windowless cabin above the car deck.")
elif input == "C":
    print(f"windowless cabin below the car deck.")
else:
    print(f"Invalid cabin class")
# Ex 3
gender = input("Enter your gender: ")
if gender == "males":
    hemoglobin = float(input("Enter hemoglobin value: "))
    if hemoglobin < 134:
        print(f"low")
    elif hemoglobin > 167:
        print(f"high")
    else:
        print(f"normal")
elif gender == "female":
    hemoglobin = float(input("Enter hemoglobin value: "))
    if hemoglobin < 117:
        print(f"low")
    elif hemoglobin > 155:
        print(f"high")
    else:
        print(f"normal")
else:
    print(f"please enter a valid gender males or females")

# Ex 4
year = int(input("Enter a year: "))
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
    print(f"Leap year")
else:
    print(f"not leap year")

# 4. While loops (while)
# Ex 1
n = 1
while n <= 1000:
    print(f"{n}")
    n += 1
# Ex 2
while True:
    inches = float(input("Enter inches: "))
    if inches >= 0:
        result = inches * 2.54
        print(f"Converted to cm: {result}")
    else:
        break
# Ex 3
numbers = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
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
    if guess == random_num:
        print(f"Correct!")
        break
    elif guess < random_num:
        print(f"Too low")
    else:
        print(f"Too high")

# Ex 5
pwd = "rules"
usr_name = "python"
n = 5
while n >= 1:
    user_input = input("Enter user name: ")
    pwd_input = input("Enter password: ")
    if user_input == usr_name and pwd_input == pwd:
        print(f"Welcome")
        break
    else:
        if n > 1:
            print(f"Incorrect! Try again! You have {n - 1}  left")
        else:
            print(f"Access denied")
    n -= 1

# Ex 6

# 5. List structures and iterative loops (for)
# Ex 1
dice = [1, 2, 3, 4, 5, 6]
sum = 0
user_input = int(input("How many dice to roll: "))
for n in range(0, user_input):
    value = dice[random.randint(0, 5)]
    print(f"value: {value}")
    sum += value
print(f"Sum of numbers: {sum}")

# Ex 2
numbers = []
sum_numbers = 0
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    else:
        number = int(user_input)
        numbers.append(number)
numbers.sort(reverse=True)
if len(numbers) > 4:
    for n in range(5):
        sum_numbers += numbers[n]
print(f"Sum is: {sum}")

# Ex 3

# Ex 4
cities = []
for i in range(5):
    user_input = input("Enter a city: ")
    cities.append(user_input)
for city in cities:
    print(f"{city}")


# 6. Functions
# Ex 1
def random_dice():
    return random.randint(1, 6)


roll_count = 0
while True:
    roll = random_dice()
    roll_count += 1
    print(f"Roll: {roll_count} Value: {roll}")
    if roll == 6:
        break
# Ex 2
sides = 21


def random_dice(sides):
    return random.randint(1, sides)


roll_count = 0
while True:
    roll = random_dice(sides)
    roll_count += 1
    print(f"Roll: {roll_count} Value: {roll}")
    if roll == sides:
        break


# Ex 3
def gallon_to_liter(gallons):
    return gallons * 3.78541


while True:
    gallons = float(input("Enter gallons to be converted: "))
    if gallons < 0:
        break
    result = gallon_to_liter(gallons)
    print(f"{gallons} gallons equal {result} liters")


# Ex 4
def sum_lists(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


test1 = sum_lists([1, 2, 3, 4, 5])
test2 = sum_lists([])
print(f"{test1}")
print(f"{test2}")


# Ex 5
def even_lists_only(numbers):
    new_numbers = []
    for number in numbers:
        if number % 2 == 0:
            new_numbers.append(number)


test1 = even_lists_only([1, 2, 3, 4, 5])
test2 = even_lists_only([])
print(f"{test1}")
print(f"{test2}")
# Ex 6
first_pizza = float(input("Enter diameter of first pizza: "))
first_price = float(input("Enter price of first pizza: "))
second_pizza = float(input("Enter diameter of second pizza: "))
second_price = float(input("Enter price of second pizza: "))


def unit_price(diameter, price):
    pi_value = math.pi
    radius_value = diameter / 2
    area = pi_value * radius_value * radius_value
    conversion_factor = 10000
    area_in_m2 = area / conversion_factor
    unit_price = price / area_in_m2
    return unit_price


first_pizza_unit_price = unit_price(first_pizza, first_price)
second_pizza_unit_price = unit_price(second_pizza, second_price)
if first_pizza_unit_price < second_pizza_unit_price:
    print(f"The pizza 1 has better value!")
elif first_pizza_unit_price > second_pizza_unit_price:
    print(f"The pizza 2 has better unit value!")
else:
    print(f"2 pizza has the same unit value!")
# 7. Tuple, set, and dictionary
# Ex 1
seasons = "spring", "summer", "autumn", "winter"
while True:
    user_input = int(input("Enter a number of a month: "))
    if user_input >= 1 and user_input <= 12:
        if user_input == 12 or (user_input >= 1 and user_input <= 2):
            print(f"{seasons[3].capitalize()}")
        elif user_input >= 3 and user_input <= 5:
            print(f"{seasons[0].capitalize()}")
        elif user_input >= 6 and user_input <= 8:
            print(f"{seasons[1].capitalize()}")
        else:
            print(f"{seasons[2].capitalize()}")
        break
    else:
        print(f"Enter number in range 1-12")
# Ex 2
names = set()
while True:
    user_input = input("Enter a name: ")
    if user_input == "":
        break
    if len(names) == 0:
        print(f"New name")
        names.add(user_input)
    else:
        if user_input in names:
            print(f"Existing name")
        else:
            print(f"New name")
            names.add(user_input)
