# Check Leap Year
# Take a year as input and check if it is a leap year.

try:
    year = int(input("Enter a year: "))
    if year % 400 == 0:
        print(f"{year} is a leap year.")
    elif year % 100 == 0:
        print(f"{year} is not a leap year.")
    elif year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Invalid input. Please enter a valid year.")
