# Temperature Converter Function
# Create functions that convert Celsius to Fahrenheit and Fahrenheit to Celsius.

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter choice (1/2): ")

try:
    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C is {c_to_f(c):.2f}°F")
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F is {f_to_c(f):.2f}°C")
    else:
        print("Invalid choice.")
except ValueError:
    print("Invalid input.")
