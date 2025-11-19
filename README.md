# college_project

# Dice Rolling Simulator

This is a small Python project that simulates rolling a six-sided dice. You can roll the dice as many times as you want and see the result for each roll. It's a fun little program to practice Python basics like random numbers, loops, and user input.

## Features

- Rolls a six-sided dice and shows the result.
- Lets you roll the dice repeatedly until you decide to stop.
- Simple text-based interface, easy to use.

## How to Use

1. Run the Python script.
2. Press Enter when prompted to roll the dice.
3. See what number you rolled.
4. Choose if you want to roll again by typing 'y' or 'n


## Python Concepts Used

- `random` module for generating random numbers.
- Functions and loops for clean and reusable code.
- Basic input/output for interacting with the user.

## Getting Started

Make sure you have Python installed. This script works with Python 3.

## Code

    import random

    def roll_dice():
    # This picks a random number between 1 and 6 like a dice roll
    return random.randint(1, 6)

    ("Hey! Let's roll the dice.")
    while True:
    input("Press Enter to roll...")
    result = roll_dice()
    print(f"You rolled a {result}!")

    again = input("Want to roll again? (y/n): ").lower()
    if again != 'y':
        print("Okay, thanks for playing. Bye!")
        break







