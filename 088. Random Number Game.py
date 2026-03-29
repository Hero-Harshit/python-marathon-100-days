# Random Number Game
# Use Python's random module to generate a number and let the user guess it.

import random

target = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid integer.")
