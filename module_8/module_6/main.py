import math
import random


# 6. Functions
# Ex 1
def random_dice():
    return random.randint(1, 6)


roll_count = 1
while True:
    roll = random_dice()
    print(f"Roll: {roll_count} Value: {roll}")
    roll_count += 1
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
    print(f"{gallons} gallons equal {result:.2f} liters")


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
