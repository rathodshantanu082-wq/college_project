import random

def roll_dice():
    # This picks a random number between 1 and 6 like a dice roll
    return random.randint(1, 6)

print("Hey! Let's roll the dice.")
while True:
    input("Press Enter to roll...")
    result = roll_dice()
    print(f"You rolled a {result}!")

    again = input("Want to roll again? (y/n): ").lower()
    if again != 'y':
        print("Okay, thanks for playing. Bye!")
        break

