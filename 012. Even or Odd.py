# Even or Odd
# Take an integer and determine if it is even or odd.

try:
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
except ValueError:
    print("Invalid input. Please enter an integer.")
