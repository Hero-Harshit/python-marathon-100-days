# Even/Odd Function
# Create a function that takes a number and returns whether it is even or odd.

def is_even(number):
    return number % 2 == 0

try:
    num = int(input("Enter an integer: "))
    if is_even(num):
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")
except ValueError:
    print("Please enter a valid integer.")
