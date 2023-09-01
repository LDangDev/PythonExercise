import mysql.connector
import math
from geopy import distance


# 8. Using relational databases
# Ex 1
def getAirportNameAndLocation(ICAO_code):
    sql_query = (
        "select ident, airport.name as airport_name, country.name as country_name "
    )
    sql_query += (
        "from airport inner join country on country.iso_country = airport.iso_country "
    )
    sql_query += f"where airport.ident = '{ICAO_code}';"

    cursor = connection.cursor()
    cursor.execute(sql_query)
    response = cursor.fetchall()
    for row in response:
        print(f"Airport name is: {row[1]} and location is {row[2]}")


connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="dbuser",
    password="pAs5w_0rD",
    autocommit=True,
)


ICAO_code = input("Enter ICAO code of an airport: ")
getAirportNameAndLocation(ICAO_code)


# Ex 2
def getAreaCodeInput(area_code):
    upper_area_code = area_code
    sql = "select ident, type, country.name as country_name, count(*) as total from airport "
    sql += "inner join country on airport.iso_country = country.iso_country "
    sql += f"where country.iso_country = '{upper_area_code}' group by type;"

    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    result = f"{response[0][2]} has "
    for row in response:
        if row[1] == "heliport":
            result += f"{row[3]} helicopter airports, "
        else:
            result += f"{row[3]} {row[1]}, "
    print(result.rstrip(", "))


connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="dbuser",
    password="pAs5w_0rD",
    autocommit=True,
)
area_code_input = input("Enter the area code: ").upper()
getAreaCodeInput(area_code_input)

# Ex 3


def calculate_airports_distance(first_ICAO_code, second_ICAO_code):
    sql = f"select ident, name, latitude_deg , longitude_deg from airport where ident = '{first_ICAO_code}' or ident = '{second_ICAO_code}';"

    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    first_airport = response[0][2], response[0][3]
    second_airport = response[1][2], response[1][3]

    airports_distance = distance.distance(first_airport, second_airport).km
    print(
        f"The distance between {response[0][1]} and {response[1][1]} is {airports_distance:.2f} km"
    )


connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="dbuser",
    password="pAs5w_0rD",
    autocommit=True,
)

first_ICAO_code = input("Enter ICAO code of the first airport: ").upper()
second_ICAO_code = input("Enter ICAO code of the second airport: ").upper()

calculate_airports_distance(first_ICAO_code, second_ICAO_code)
