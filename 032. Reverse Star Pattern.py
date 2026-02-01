# Reverse Star Pattern
# Print an inverted right-angled triangle of stars.

try:
    rows = int(input("Enter the number of rows: "))
    for i in range(rows, 0, -1):
        print("*" * i)
except ValueError:
    print("Invalid input.")
