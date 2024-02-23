# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:36:26 2024

@author: walters
"""

def is_prime(number):
    """Checks if a given number is prime."""
    if number <= 1:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def main():
    try:
        user_input = int(input("Enter a positive integer: "))
        if user_input <= 0:
            print("Please enter a positive integer greater than 1.")
            return
        if is_prime(user_input):
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
