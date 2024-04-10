#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
/python/<text>: display “Python ”, followed by the value of the text variable
/number_template/<n>: display a HTML page only if n is an integer
/number_odd_or_even/<n>: display a HTML page only if n is an integer
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """display Hello HBNB!"""
    return "<p>Hello HBNB!</p>"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Display HBNB"""
    return "<p>HBNB</p>"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    """display C followed by the value of the text variable"""
    string = "<p>C %s</p>" % text
    string = string.replace("_", " ")
    return string


@app.route("/python", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def Python_is_cool(text):
    """display Python, followed by the value of text"""
    string1 = "<p>Python %s</p>" % text
    string1 = string1.replace("_", " ")
    return string1


@app.route("/number/<int:n>", strict_slashes=False)
def is_it_a_number(n):
    """display n is a number only if n is an integer"""
    return "<p>%d is a number</p>" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """display HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if n % 2 == 0:
        evod = "even"
    else:
        evod = "odd"
    return render_template("6-number_odd_or_even.html", n=n, evod=evod)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
