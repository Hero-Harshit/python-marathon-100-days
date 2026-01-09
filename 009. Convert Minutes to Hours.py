# Convert Minutes to Hours
# Take a number of minutes and convert it into hours and remaining minutes.

try:
    total_minutes = int(input("Enter total minutes: "))
    if total_minutes < 0:
        print("Minutes cannot be negative.")
    else:
        hours = total_minutes // 60
        minutes = total_minutes % 60
        print(f"{total_minutes} minutes is equal to {hours} hours and {minutes} minutes.")
except ValueError:
    print("Invalid input. Please enter an integer.")
