# Menu-Driven Function Program
# Create a program where the user selects an operation from a menu and your functions perform the requested operation.

def square(n): return n ** 2
def cube(n): return n ** 3

while True:
    print("\n1. Square a number")
    print("2. Cube a number")
    print("3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        try:
            num = float(input("Enter number: "))
            print(f"Square is: {square(num)}")
        except:
            print("Invalid number.")
    elif choice == '2':
        try:
            num = float(input("Enter number: "))
            print(f"Cube is: {cube(num)}")
        except:
            print("Invalid number.")
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
