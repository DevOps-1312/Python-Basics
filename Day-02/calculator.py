## Simple Calculator Program
# This program performs basic arithmetic operations using functions: addition, subtraction, multiplication, and division.

def addition(a, b):
    add = a + b
    print(f"The sum of {a} and {b} is: {add}")

def subtraction(a, b):
    sub = a - b
    print(f"The difference between {a} and {b} is: {sub}")

def multiplication(a, b):
    mul = a * b
    print(f"The product of {a} and {b} is: {mul}")

def division(a, b):
    if b != 0:
        div = a / b
        print(f"The quotient of {a} and {b} is: {div}")
    else:
        print("Error: Division by zero is not allowed.")


def get_numbers():
    global num1, num2
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        if operation == '+':
            addition(num1, num2)
        elif operation == '-':
            subtraction(num1, num2)
        elif operation == '*':
            multiplication(num1, num2)
        elif operation == '/':
            division(num1, num2)
        else:
            print("Invalid operation selected.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    get_numbers()

