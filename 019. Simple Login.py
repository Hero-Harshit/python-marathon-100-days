# Simple Login
# Ask the user for a username and password, and check them against hardcoded values.

correct_username = "admin"
correct_password = "password123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful! Welcome.")
else:
    print("Login failed. Incorrect username or password.")
