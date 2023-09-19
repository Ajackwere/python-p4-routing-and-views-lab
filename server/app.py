#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views </h1>'
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'Printed string: {paramter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(1, parameter + 1))
    return f'Counting numbers from 1 to {parameter}:\n{numbers}'

@app.route('/math/<float:num1><operation><float:num2>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
