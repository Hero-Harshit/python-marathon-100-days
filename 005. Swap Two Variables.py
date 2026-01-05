# Swap Two Variables
# Take two inputs, swap their values, and print them.

a = input("Enter the first value (a): ")
b = input("Enter the second value (b): ")

print(f"Before swapping: a = {a}, b = {b}")

# Swapping
temp = a
a = b
b = temp

print(f"After swapping: a = {a}, b = {b}")
