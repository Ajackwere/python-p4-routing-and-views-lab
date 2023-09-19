#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views </h1>'


@app.route('/print/<string:parameter>')
def print_string(parameter):
    print('parameter')
    return f'{parameter}'


@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(1, parameter + 1))
    return f'Counting numbers from 1 to {parameter}:\n{numbers}'


@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
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
            return 'Division by zero is not possible'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    return f'Result of {num1} {operation} {num2} is {result}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
