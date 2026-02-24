# Count Occurrences
# Count how many times a specific number appears in a list.

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = user_input.split()
target = input("Enter the number to count: ")

count = 0
for num in numbers:
    if num == target:
        count += 1

print(f"The number {target} appears {count} time(s) in the list.")
