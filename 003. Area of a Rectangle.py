# Area of a Rectangle
# Take length and width from the user and calculate the area.

try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    if length < 0 or width < 0:
        print("Length and width must be positive numbers.")
    else:
        area = length * width
        print(f"The area of the rectangle is: {area}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
