# Your First Function
# Create a function that takes two numbers and returns their sum.

def add_numbers(a, b):
    return a + b

print("--- Addition Program ---")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum is: {result}")
except ValueError:
    print("Please enter valid numbers.")
