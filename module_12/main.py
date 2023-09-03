import requests
import json

# Ex 1
try:
    request = "https://api.chucknorris.io/jokes/random"
    response = requests.get(request)
    if response.status_code == 200:
        # convert json type to python data type
        data = response.json()
        print(data["value"])
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")
# Ex 2
city_name = input("Enter a city name to check the corresponding weather: ").capitalize()
API_key = "cf9b18c313529565bde1114489b7b076"

try:
    request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
    response = requests.get(request)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        print(f"Temperature of {city_name} is: {data['main']['temp']} degree Celsius")
    else:
        print(f"{city_name} is not valid! Please enter a correct city name")
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")
