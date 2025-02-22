#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:word>")
def print_string(word):
    print(word)
    return word

@app.route("/count/<int:number>")
def count(number):
    numlist = list(range(number))
    stringlist = map(str, numlist)
    num_per_line = "\n".join(stringlist) + "\n"
    print(type(num_per_line))
    print(num_per_line)
    return num_per_line

@app.route("/math/<int:num1><string:operation><int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return f"{num1 + num2}"
    elif operation == "-":
        return f"{num1 - num2}" 
    elif operation == "*":
        return f"{num1 * num2}"
    elif operation == "div":
        return f"{num1 / num2}"
    elif operation == "%":
        return f"{num1 % num2}"
    else:
        return "Invalid operation"

if __name__ == '__main__':
    app.run(port=5555, debug=True)


