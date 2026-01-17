# Grade Calculator
# Take a student's percentage and print their grade (A, B, C, D, or F).

try:
    percentage = float(input("Enter your percentage (0-100): "))
    if percentage < 0 or percentage > 100:
        print("Invalid percentage. Please enter a value between 0 and 100.")
    elif percentage >= 90:
        print("Grade: A")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
except ValueError:
    print("Invalid input.")
