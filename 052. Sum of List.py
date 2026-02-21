# Sum of List
# Take a list of numbers and calculate their sum.

user_input = input("Enter numbers separated by spaces: ")
num_strings = user_input.split()
total = 0

for s in num_strings:
    try:
        total += float(s)
    except ValueError:
        print(f"Skipping invalid number: {s}")

print(f"The sum of the numbers is: {total}")
