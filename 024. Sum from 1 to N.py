# Sum from 1 to N
# Take a number N and calculate the sum of all numbers from 1 to N.

try:
    n = int(input("Enter a positive integer N: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        total = 0
        for i in range(1, n + 1):
            total += i
        print(f"The sum of numbers from 1 to {n} is: {total}")
except ValueError:
    print("Invalid input.")
