# Basic Calculator
# Take two numbers and an operator from the user and perform the calculation.

try:
    num1 = float(input("Enter the first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"Result: {num1 / num2}")
    else:
        print("Invalid operator.")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
