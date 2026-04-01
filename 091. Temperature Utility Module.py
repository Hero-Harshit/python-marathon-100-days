# Temperature Utility Module
# Create your own Python module containing temperature-conversion functions and import it into another Python file.
# Note: For simplicity in this single file, we simulate a module by defining the functions here.

class TempModule:
    @staticmethod
    def c_to_f(c): return (c * 9/5) + 32
    
    @staticmethod
    def f_to_c(f): return (f - 32) * 5/9

print("Using simulated Temperature Module:")
try:
    c = float(input("Enter Celsius to convert: "))
    print(f"Result: {TempModule.c_to_f(c):.2f}°F")
except ValueError:
    print("Invalid input.")
