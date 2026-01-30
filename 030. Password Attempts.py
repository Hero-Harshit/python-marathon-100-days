# Password Attempts
# Allow the user 3 attempts to enter a correct password.

correct_password = "secretpassword"
attempts = 3

while attempts > 0:
    password = input(f"Enter password ({attempts} attempts left): ")
    if password == correct_password:
        print("Access Granted.")
        break
    else:
        attempts -= 1
        print("Incorrect password.")

if attempts == 0:
    print("Account locked due to too many failed attempts.")
