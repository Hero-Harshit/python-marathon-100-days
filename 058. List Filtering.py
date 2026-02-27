# List Filtering
# Take a list of numbers and create a new list containing only numbers greater than 10.

user_input = input("Enter numbers separated by spaces: ")
num_strings = user_input.split()
filtered_list = []

for s in num_strings:
    try:
        num = float(s)
        if num > 10:
            filtered_list.append(num)
    except ValueError:
        pass

print(f"Numbers greater than 10: {filtered_list}")
