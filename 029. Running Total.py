# Running Total
# Keep taking numbers from the user and printing their sum until they enter '0'.

total = 0
print("Enter numbers to add to the total. Enter '0' to stop.")

while True:
    user_input = input("Enter a number: ")
    if user_input == '0':
        print(f"Final total is: {total}")
        break
    try:
        num = float(user_input)
        total += num
        print(f"Current total: {total}")
    except ValueError:
        print("Please enter a valid number.")
