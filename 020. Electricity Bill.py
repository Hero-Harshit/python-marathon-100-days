# Electricity Bill
# Calculate an electricity bill based on different per-unit charges for different consumption ranges.

try:
    units = float(input("Enter the number of units consumed: "))
    if units < 0:
        print("Units cannot be negative.")
    else:
        bill = 0
        if units <= 100:
            bill = units * 5
        elif units <= 200:
            bill = (100 * 5) + ((units - 100) * 8)
        else:
            bill = (100 * 5) + (100 * 8) + ((units - 200) * 10)
        
        print(f"Total Electricity Bill: ${bill:.2f}")
except ValueError:
    print("Invalid input.")
