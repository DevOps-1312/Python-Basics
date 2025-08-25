# Cal_cmd_Arg's.py
# This script performs basic arithmetic operations based on command line arguments.
# It takes two numbers and an operation as command line arguments and prints the result.

import sys

def addition(a, b):
    add = a + b
    return f"The sum of {a} and {b} is: {add}"

def subtraction(a, b):
    sub = a - b
    return f"The difference between {a} and {b} is: {sub}"

def multiplication(a, b):
    mul = a * b
    return f"The product of {a} and {b} is: {mul}"

def division(a, b):
    if b != 0:
        div = a / b
        return f"The quotient of {a} and {b} is: {div}"
    else:
        return "Error: Division by zero is not allowed."
    
a =  float(sys.argv[1])
operation = sys.argv[2]
b =  float(sys.argv[3])

if operation == '+' or operation == 'add':
    print(addition(a, b))
elif operation == '-' or operation == 'subtract':
    print(subtraction(a, b))
elif operation == '*' or operation == 'multiply':
    print(multiplication(a, b))
elif operation == '/' or operation == 'divide':
    print(division(a, b))
else:
    print("Invalid operation selected.")


