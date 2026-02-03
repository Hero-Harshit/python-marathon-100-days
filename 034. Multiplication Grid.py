# Multiplication Grid
# Print a 5x5 grid of numbers using nested loops.

print("--- 5x5 Multiplication Grid ---")
for i in range(1, 6):
    row_str = ""
    for j in range(1, 6):
        # Format to align nicely
        row_str += f"{i * j:4}"
    print(row_str)
