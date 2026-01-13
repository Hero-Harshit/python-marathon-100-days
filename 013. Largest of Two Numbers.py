# Largest of Two Numbers
# Take two numbers and print the larger one.

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if num1 > num2:
        print(f"The larger number is {num1}")
    elif num2 > num1:
        print(f"The larger number is {num2}")
    else:
        print("Both numbers are equal.")
except ValueError:
    print("Invalid input.")
