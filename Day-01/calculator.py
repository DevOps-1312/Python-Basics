# calculator.py
# This script performs basic arithmetic operations: addition, subtraction, multiplication, and division.
print("Welcome to the Basic Calculator!")
num1 = int (input("Enter first number = "))
num2 = int (input("Enter Second number = "))

sum_of_num = num1 + num2
print("Sum of 2 numbers = ", sum_of_num)

diff_of_num = num1 - num2
print("Diff of 2 numbers = ",diff_of_num)

prod_of_num = num1 * num2
print("Product of 2 numbers = ", prod_of_num)

div_of_num = num1 / num2
print("Division of 2 numbers = ",div_of_num)

# Round off the division result
div_of_num_rounded = round(div_of_num)
print("Rounded Division of 2 numbers = ", div_of_num_rounded)

# absolute value of the difference
abs_diff = abs(diff_of_num)
print("Absolute value of the difference = ", abs_diff)

