# Username Generator
# Combine a user's first name, last name, and birth year to create a username.

first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()
year = input("Enter your birth year: ").strip()

username = f"{first.lower()}_{last.lower()}{year}"
print(f"Your generated username is: {username}")
