# Add Two Numbers
# Take two numbers from the user and print their sum.

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}")
except ValueError:
    print("Invalid input. Please enter numbers only.")
