import math
import random


numbers = []
sum_numbers = 0
while True:
    user_input = input("Enter a number: ")
    if(user_input == ''):
        break
    else:
        number = int(user_input)
        numbers.append(number)
numbers.sort(reverse=True)
if len(numbers) > 4:
    for n in range(0, len(numbers)):
        sum_numbers += numbers[n]
print(f"Sum is: {sum}")




