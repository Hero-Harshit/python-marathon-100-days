# Celsius to Fahrenheit
# Take a temperature in Celsius and convert it to Fahrenheit.

try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
except ValueError:
    print("Invalid input. Please enter a valid number.")
