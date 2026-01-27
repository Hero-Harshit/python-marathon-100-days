# Multiplication Table
# Print the multiplication table for a given number using a for loop.

try:
    num = int(input("Enter a number: "))
    print(f"--- Multiplication Table for {num} ---")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Invalid input. Please enter an integer.")
