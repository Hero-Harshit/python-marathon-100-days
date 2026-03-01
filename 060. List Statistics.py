# List Statistics
# Calculate the mean, median, and mode of a list of numbers.

import statistics

user_input = input("Enter numbers separated by spaces: ")
try:
    numbers = [float(x) for x in user_input.split()]
    if not numbers:
        print("List is empty.")
    else:
        mean = statistics.mean(numbers)
        median = statistics.median(numbers)
        try:
            mode = statistics.mode(numbers)
            print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
        except statistics.StatisticsError:
            print(f"Mean: {mean}, Median: {median}, Mode: No unique mode found.")
except ValueError:
    print("Please enter valid numbers.")
