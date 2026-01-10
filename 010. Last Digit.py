# Last Digit
# Take a number and print its last digit.

try:
    num = int(input("Enter an integer: "))
    # Use abs() to handle negative numbers properly
    last_digit = abs(num) % 10
    print(f"The last digit of {num} is {last_digit}")
except ValueError:
    print("Invalid input. Please enter an integer.")
