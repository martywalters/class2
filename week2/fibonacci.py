# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:33:59 2024

@author: walters
"""

def generate_fibonacci(n):
    """Generates the first n Fibonacci numbers using recursion."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = generate_fibonacci(n - 1)
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
        return fib_sequence

def main():
    try:
        num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
            return
        fibonacci_numbers = generate_fibonacci(num_terms)
        print(f"The first {num_terms} Fibonacci numbers are:")
        print(fibonacci_numbers)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
