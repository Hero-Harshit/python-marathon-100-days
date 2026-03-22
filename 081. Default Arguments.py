# Default Arguments
# Create a greeting function where the user's name is optional and a default name is used when none is provided.

def greet(name="Guest"):
    print(f"Hello, {name}! Welcome.")

user_input = input("Enter your name (or press Enter to use default): ")
if user_input.strip() == "":
    greet()
else:
    greet(user_input)
