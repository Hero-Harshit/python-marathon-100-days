# Dictionary Lookup
# Ask the user for a key and retrieve the corresponding value from a dictionary.

capitals = {
    "usa": "Washington D.C.",
    "france": "Paris",
    "japan": "Tokyo",
    "india": "New Delhi"
}

country = input("Enter a country name (USA, France, Japan, India): ").lower()

# Using get() to handle cases where the key doesn't exist safely
capital = capitals.get(country)

if capital:
    print(f"The capital is {capital}.")
else:
    print("Sorry, that country is not in the dictionary.")
