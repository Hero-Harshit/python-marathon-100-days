# Separate Even and Odd
# Take a list of numbers and split it into two separate lists: one for evens and one for odds.

user_input = input("Enter integers separated by spaces: ")
num_strings = user_input.split()

evens = []
odds = []

for s in num_strings:
    try:
        num = int(s)
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    except ValueError:
        print(f"Skipping invalid integer: {s}")

print(f"Even numbers: {evens}")
print(f"Odd numbers: {odds}")
