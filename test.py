import math
import random


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
