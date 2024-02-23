# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:31:38 2024

@author: walters
"""

import random

def generate_random_number():
    """Generates a random 4-digit number with non-repeating digits."""
    return random.sample(range(10), 4)

def evaluate_guess(secret_number, user_guess):
    """Evaluates the user's guess and returns the number of hearts and spades."""
    hearts = 0
    spades = 0
    for i in range(4):
        if user_guess[i] == secret_number[i]:
            hearts += 1
        elif user_guess[i] in secret_number:
            spades += 1
    return hearts, spades

def main():
    secret_number = generate_random_number()
    num_guesses = 0

    print("Welcome to the Hearts and Spades game!")
    print("Guess a 4-digit number (each digit should be unique).")

    while True:
        user_input = input("Enter your guess: ")
        try:
            user_guess = [int(digit) for digit in user_input]
            if len(user_guess) != 4 or len(set(user_guess)) != 4:
                print("Invalid input. Please enter a 4-digit number with unique digits.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid 4-digit number.")
            continue

        num_guesses += 1
        hearts, spades = evaluate_guess(secret_number, user_guess)
        print(f"Hearts: {hearts}, Spades: {spades}")

        if hearts == 4:
            print(f"Congratulations! You guessed the correct number {secret_number} in {num_guesses} guesses.")
            break

if __name__ == "__main__":
    main()
