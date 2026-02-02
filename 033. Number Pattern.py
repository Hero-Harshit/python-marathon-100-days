# Number Pattern
# Print a number pyramid (e.g., 1, 22, 333).

try:
    rows = int(input("Enter the number of rows: "))
    for i in range(1, rows + 1):
        print(str(i) * i)
except ValueError:
    print("Invalid input.")
