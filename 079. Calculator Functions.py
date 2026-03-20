# Calculator Functions
# Create separate functions for addition, subtraction, multiplication, and division.

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Addition: {add(num1, num2)}")
    print(f"Subtraction: {subtract(num1, num2)}")
    print(f"Multiplication: {multiply(num1, num2)}")
    print(f"Division: {divide(num1, num2)}")
except ValueError:
    print("Invalid input.")
