import random

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