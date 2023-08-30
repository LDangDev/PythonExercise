import math
import random


def even_lists_only(numbers):
    new_numbers = []
    for number in numbers:
        if number % 2 == 0:
            new_numbers.append(number)
    return new_numbers
test1 = even_lists_only([1, 2, 3, 4, 5])
test2 = even_lists_only([])
print(f"{test1}")
print(f"{test2}")




