# Password Validator Function
# Create a function that checks whether a password satisfies rules such as minimum length, uppercase character, lowercase character, digit, and special character.

def is_valid_password(pwd):
    if len(pwd) < 8:
        return False, "Password must be at least 8 characters long."
    if not any(c.isupper() for c in pwd):
        return False, "Password must contain at least one uppercase letter."
    if not any(c.islower() for c in pwd):
        return False, "Password must contain at least one lowercase letter."
    if not any(c.isdigit() for c in pwd):
        return False, "Password must contain at least one digit."
    special_chars = "!@#$%^&*()-_+="
    if not any(c in special_chars for c in pwd):
        return False, "Password must contain at least one special character."
    
    return True, "Password is valid!"

password = input("Enter a password to validate: ")
is_valid, message = is_valid_password(password)
print(message)
