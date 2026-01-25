# Count Digits
# Take a number and count how many digits it has.

num = input("Enter a number: ")

# Remove the negative sign if it exists
if num.startswith('-'):
    num = num[1:]

if num.isdigit():
    print(f"The number has {len(num)} digit(s).")
else:
    print("Invalid input. Please enter a valid integer.")
