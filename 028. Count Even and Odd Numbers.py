# Count Even and Odd Numbers
# Take a list of numbers from the user and count how many are even and how many are odd.

user_input = input("Enter a list of numbers separated by spaces: ")
numbers_str = user_input.split()

even_count = 0
odd_count = 0

for num_str in numbers_str:
    if num_str.isdigit() or (num_str.startswith("-") and num_str[1:].isdigit()):
        if int(num_str) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")
