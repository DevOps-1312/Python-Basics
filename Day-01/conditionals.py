# This script performs basic arithmetic operations based on user input.
while True:
    try:
        num1 = int(input("Enter first number = "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer for the first number.")

while True:
    try:
        num2 = int(input("Enter Second number = "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer for the second number.")

choice = input("Enter the operation: (operations +,-.*./.%) = ")

if choice == "+":
    sum_of_num = num1 + num2
    print("Addition: ",sum_of_num)
elif choice == "-":
    diff_of_num = num1 - num2
    print("Subtraction: ",diff_of_num)
elif choice == "*":
    prod_of_num = num1 * num2
    print("Multiplication: ",prod_of_num)
elif choice == "/":
    div_of_num = num1 / num2
    print("Division: ",div_of_num)
elif choice == "%":
    Rem_of_num =num1 % num2
    print("Reminder: ",Rem_of_num)
else:
    print("Invalid chice Please run again")