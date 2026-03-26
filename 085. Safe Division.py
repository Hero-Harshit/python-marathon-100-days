# Safe Division
# Create a calculator that handles division by zero without crashing.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"

try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    print(f"Result: {safe_divide(num1, num2)}")
except ValueError:
    print("Invalid input.")
