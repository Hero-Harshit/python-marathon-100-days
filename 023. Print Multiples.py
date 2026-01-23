# Print Multiples
# Print the first 10 multiples of a number entered by the user.

try:
    num = int(input("Enter a number to find its multiples: "))
    print(f"The first 10 multiples of {num} are:")
    for i in range(1, 11):
        print(num * i)
except ValueError:
    print("Invalid input. Please enter an integer.")
