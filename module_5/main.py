import random
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
        print(f"{numbers[n]}")
else:
    print(f"Please enter at least 5 numbers")

# Ex 3
isPrime = True
user_input = int(input("Enter a number: "))
if(user_input == 1):
    print(f"Not a prime number")
else:
    for number in range (2, user_input):
        if(user_input % number == 0):
            print(f"Not a prime number")
            isPrime = False
            break
    if isPrime:
        print(f"Prime number")
    
# Ex 4
cities = []
for i in range(5):
    user_input = input("Enter a city: ")
    cities.append(user_input)
for city in cities:
    print(f"{city}")