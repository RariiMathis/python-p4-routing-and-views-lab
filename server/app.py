#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<parameter>')
def count(parameter):
    numbers = '\n'.join(map(str, range(parameter)))
    return numbers

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"
    elif operation == '%':
        result = num1 % num2
        
    return f"Result: {result}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)