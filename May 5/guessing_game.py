import random  # Import the random module to generate random numbers

# Generate a random number between 1 and 10 (inclusive)
number = random.randint(1, 10)

# Prompt the user to guess the number
guess = int(input("Guess a number between 1 and 10: "))

# Loop until the user guesses the correct number
while guess != number:
    if guess < number:
        print("Too low!")   # Inform the user if the guess is too small
    else:
        print("Too high!")  # Inform the user if the guess is too large
    
    # Prompt the user to guess again
    guess = int(input("Try again: "))

# User guessed the correct number
print("Congratulations! You guessed it.")
