# Star Pattern
# Print a right-angled triangle pattern of stars.

try:
    rows = int(input("Enter the number of rows for the pattern: "))
    for i in range(1, rows + 1):
        print("*" * i)
except ValueError:
    print("Invalid input. Please enter an integer.")
