# Calculate Total and Percentage
# Take marks of five subjects and calculate the total marks and percentage.

try:
    m1 = float(input("Enter marks for Subject 1: "))
    m2 = float(input("Enter marks for Subject 2: "))
    m3 = float(input("Enter marks for Subject 3: "))
    m4 = float(input("Enter marks for Subject 4: "))
    m5 = float(input("Enter marks for Subject 5: "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = (total / 500) * 100  # Assuming each subject is out of 100

    print(f"Total Marks: {total}/500")
    print(f"Percentage: {percentage}%")
except ValueError:
    print("Invalid input. Please enter numeric marks.")
