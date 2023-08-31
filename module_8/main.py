import mysql.connector


def getAirportNameAndLocation(ICAO_code):
    sql_query = f"select ident, airport.name as airport_name, country.name as country_name from airport inner join country on country.iso_country = airport.iso_country where airport.ident = '{ICAO_code}';"

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
