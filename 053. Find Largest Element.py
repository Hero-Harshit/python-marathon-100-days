# Find Largest Element
# Find the largest number in a list without using the built-in max() function.

user_input = input("Enter numbers separated by spaces: ")
num_strings = user_input.split()

if not num_strings:
    print("List is empty.")
else:
    try:
        largest = float(num_strings[0])
        for s in num_strings:
            num = float(s)
            if num > largest:
                largest = num
        print(f"The largest number is: {largest}")
    except ValueError:
        print("Please enter valid numbers.")
