# Unit Converter
# Build a small program using functions/modules that can convert between multiple units such as kilometres/miles, kilograms/pounds, and Celsius/Fahrenheit.

def km_to_miles(km): return km * 0.621371
def kg_to_lbs(kg): return kg * 2.20462
def c_to_f(c): return (c * 9/5) + 32

while True:
    print("\n1. Kilometers to Miles")
    print("2. Kilograms to Pounds")
    print("3. Celsius to Fahrenheit")
    print("4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        v = float(input("Enter km: "))
        print(f"{v} km = {km_to_miles(v):.2f} miles")
    elif choice == '2':
        v = float(input("Enter kg: "))
        print(f"{v} kg = {kg_to_lbs(v):.2f} lbs")
    elif choice == '3':
        v = float(input("Enter Celsius: "))
        print(f"{v} C = {c_to_f(v):.2f} F")
    elif choice == '4':
        break
    else:
        print("Invalid choice")
