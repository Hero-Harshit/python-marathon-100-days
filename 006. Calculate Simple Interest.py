# Calculate Simple Interest
# Take principal, rate, and time from the user and calculate simple interest.

try:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time (in years): "))

    interest = (principal * rate * time) / 100
    print(f"The simple interest is: {interest}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
