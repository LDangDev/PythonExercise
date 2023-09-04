from flask import Flask, request

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
