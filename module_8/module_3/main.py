# 3. Conditional structures (if)
# Ex 1
input = float(input("Enter length of zander(in cm): "))
if input < 42:
    print(f"Release the fish back into lake or go to jail!. The size must be at lease 42 cm to catch")
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
if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
    print(f"Leap year")
else:
    print(f"not leap year")