# Function Returning Multiple Values
# Create a function that takes a list and returns its sum, average, minimum, and maximum.

def analyze_list(numbers):
    if not numbers:
        return 0, 0, None, None
    total = sum(numbers)
    avg = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, avg, minimum, maximum

user_input = input("Enter numbers separated by spaces: ")
try:
    nums = [float(x) for x in user_input.split()]
    total, avg, minimum, maximum = analyze_list(nums)
    print(f"Sum: {total}\nAverage: {avg}\nMin: {minimum}\nMax: {maximum}")
except ValueError:
    print("Please enter valid numbers.")
