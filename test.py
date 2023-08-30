import math
import random

names = set()
while True:
	user_input = input("Enter a name: ")
	if(user_input == ''):
		break
	if (len(names) == 0):
		print(f"New name")
		names.add(user_input)
	else:
		if(user_input in names):
			print(f"Existing name")
		else:
			print(f"New name")
			names.add(user_input)

		
