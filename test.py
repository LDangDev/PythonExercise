import math
import random


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
if  first_pizza_unit_price < second_pizza_unit_price:
    print(f"The pizza 1 has better value!")
elif first_pizza_unit_price > second_pizza_unit_price:
    print(f"The pizza 2 has better unit value!")
else:
    print(f"2 pizza has the same unit value!")




