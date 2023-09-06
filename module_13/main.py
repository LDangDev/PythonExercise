from flask import Flask, request, Response
import mysql.connector
import json

# 13. Setting up a backend service with an interface
# Ex 1
app = Flask(__name__)


@app.route("/prime_number/<number>")
def check_prime(number):
    isPrime = True
    number = int(number)
    if number == 1:
        isPrime = False
        return {"Number": number, "isPrime": isPrime}
    else:
        for n in range(2, number):
            if number % n == 0:
                print(f"Not a prime number")
                isPrime = False
                break
        if isPrime:
            return {"Number": number, "isPrime": isPrime}
        else:
            return {"Number": number, "isPrime": isPrime}


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=8800)

# Ex 2


app = Flask(__name__)


@app.route("/airport/<ICAO_code>")
def getICAOCode(ICAO_code):
    try:
        sql = f"""
        select name, ident, municipality 
        from airport 
        where ident = '{ICAO_code}'
        """

        cursor = connection.cursor()
        cursor.execute(sql)
        response = cursor.fetchall()
        if not response:
            raise ValueError
        result = {
            "ICAO": response[0][1],
            "Name": response[0][0],
            "Location": response[0][2],
        }
        print(result)
        return result
    except ValueError:
        response = {"message": "Invalid ICAO code", "status": 400}
        json_response = json.dumps(response)
        http_response = Response(
            response=json_response, status=400, mimetype="application/json"
        )
        return http_response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {"message": "Invalid endpoint", "status": 404}
    json_response = json.dumps(response)
    http_response = Response(
        response=json_response, status=404, mimetype="application/json"
    )
    return http_response


connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="dbuser",
    password="pwd",
    autocommit=True,
)

if __name__ == "__main__":
    app.debug = True
    app.run(use_reloader=True, host="127.0.0.1", port=6100)
