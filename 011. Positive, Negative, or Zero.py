# Positive, Negative, or Zero
# Take a number and determine if it is positive, negative, or zero.

try:
    num = float(input("Enter a number: "))
    if num > 0:
        print(f"{num} is positive.")
    elif num < 0:
        print(f"{num} is negative.")
    else:
        print("The number is zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
