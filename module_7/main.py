# 7. Tuple, set, and dictionary
# Ex 1
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
# Ex 2
names = set()
while True:
    user_input = input("Enter a name: ")
    if user_input == "":
        break
    if len(names) == 0:
        print(f"New name")
        names.add(user_input)
    else:
        if user_input in names:
            print(f"Existing name")
        else:
            print(f"New name")
            names.add(user_input)
# Ex 3
airports = {
    "Helsinki Vantaa Airport": "EFHK",
    "Charles de Gaulle International Airport": "LFPG",
    "Tan Son Nhat International Airport": "VVTS",
    "Hartsfield-Jackson Atlanta International Airport": "KATL",
    "Dubai International Airport": "OMDB",
    "Heathrow Airport": "EGLL",
    "Amsterdam Airport Schiphol": "EHAM",
    "Tokyo Haneda Airport": "RJTT",
    "Singapore Changi Airport": "WSSS",
    "Munich Airport": "EDDM",
    "Sydney Airport": "YSSY",
}

while True:
    isFound = False
    options = input(
        "Do you want to enter a new airport? Or fetch the information? Or Quit? Choose E or F or Q: "
    ).upper()
    if options == "E":
        name_airport = input("Enter name of airport: ")
        if name_airport in airports:
            print(f"Airport name exist in database")
            print(f"Airport {name_airport} and ICAO code {airports[name_airport]}")
        else:
            ICAO_input = input("Enter ICAO code: ")
            airports[name_airport] = ICAO_input
            print(f"Added new airport {name_airport} and new ICAO code {ICAO_input}")
    elif options == "F":
        ICAO_fetch = input("Enter ICAO code for fetching: ")
        for name in airports:
            if airports[name] == ICAO_fetch:
                isFound = True
                print(f"Airport {airports[name]} is found in database")
        if not isFound:
            print(f"Does not found any match airport in database")
    else:
        break
