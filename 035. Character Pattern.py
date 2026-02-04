# Character Pattern
# Print a pattern using letters (e.g., A, BB, CCC).

try:
    rows = int(input("Enter the number of rows (1-26): "))
    if 1 <= rows <= 26:
        # 65 is the ASCII value for 'A'
        for i in range(1, rows + 1):
            letter = chr(64 + i)
            print(letter * i)
    else:
        print("Please enter a number between 1 and 26.")
except ValueError:
    print("Invalid input.")
