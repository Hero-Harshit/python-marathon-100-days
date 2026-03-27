# Safe Integer Input
# Create a program that repeatedly asks the user for an integer until they enter a valid number.

def get_integer():
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            return user_input
        except ValueError:
            print("That's not a valid integer. Try again.")

number = get_integer()
print(f"You successfully entered: {number}")
