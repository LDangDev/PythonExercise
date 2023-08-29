import math
import random


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



