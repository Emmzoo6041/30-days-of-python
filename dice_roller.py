import random

# Function to simulate rolling a single dice
def roll_dice():
    return random.randint(1, 6)

# Function to simulate rolling a dice multiple times
def roll_dice_multiple(times):
    results = []
    for _ in range(times):
        results.append(roll_dice())
    return results

# Simulate rolling a single dice
single_roll = roll_dice()
print(f"Single roll result: {single_roll}")

# Simulate rolling a dice 10 times
multiple_rolls = roll_dice_multiple(10)
print(f"Multiple rolls result: {multiple_rolls}")

