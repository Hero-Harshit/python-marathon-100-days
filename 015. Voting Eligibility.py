# Voting Eligibility
# Take age as input and print whether the user is eligible to vote (18 or older).

try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("Age cannot be negative.")
    elif age >= 18:
        print("You are eligible to vote!")
    else:
        print(f"You are not eligible. Wait {18 - age} more year(s).")
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")
