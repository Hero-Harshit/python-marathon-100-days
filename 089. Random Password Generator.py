# Random Password Generator
# Use Python's standard library to generate a random password based on a requested length.

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter the desired password length (e.g., 8-16): "))
    if length < 4:
        print("Password should be at least 4 characters long.")
    else:
        print(f"Generated Password: {generate_password(length)}")
except ValueError:
    print("Invalid input.")
