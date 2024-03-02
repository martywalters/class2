# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:33:59 2024

@author: walters
"""

def fib(n):
    """Generates the first n Fibonacci numbers using recursion."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence =fib(n - 1)
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
        return fib_sequence

def main():
    num_items = int(input("Enter the number of Fibonacci numbers to generate: "))
    if num_items <= 0:
        print("Enter a positive integer.")
        return
    fib_numbers = fib(num_items) 
    print('The first ' + str(num_items) + ' Fibonacci numbers  are:')
    print(' '.join(str(x) for x in fib_numbers))

if __name__ == "__main__":
    main()
