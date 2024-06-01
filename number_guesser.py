import random

def guess_number():
    # Step 1: The computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Step 2: Initialize variables
    user_guess = None
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")
    
    # Step 3: The game loop
    while user_guess != number_to_guess:
        # Step 4: Prompt the user for a guess
        user_guess = input("Enter your guess: ")
        
        # Step 5: Check if the input is a valid number
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        # Convert user input to an integer
        user_guess = int(user_guess)
        attempts += 1
        
        # Step 6: Give feedback to the user
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")

# Step 7: Start the game
guess_number()

