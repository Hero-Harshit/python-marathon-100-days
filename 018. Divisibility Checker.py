# Divisibility Checker
# Take a number and check if it is divisible by both 3 and 5.

try:
    num = int(input("Enter an integer: "))
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is divisible by both 3 and 5.")
    else:
        print(f"{num} is NOT divisible by both 3 and 5.")
except ValueError:
    print("Invalid input. Please enter an integer.")
