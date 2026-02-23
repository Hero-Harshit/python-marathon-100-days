# Find Smallest Element
# Find the smallest number in a list without using the built-in min() function.

user_input = input("Enter numbers separated by spaces: ")
num_strings = user_input.split()

if not num_strings:
    print("List is empty.")
else:
    try:
        smallest = float(num_strings[0])
        for s in num_strings:
            num = float(s)
            if num < smallest:
                smallest = num
        print(f"The smallest number is: {smallest}")
    except ValueError:
        print("Please enter valid numbers.")
