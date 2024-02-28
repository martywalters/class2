# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:36:26 2024

@author: walters
"""

def is_prime(num):
    if num <= 1:
        return False
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False
    return True


def main():
        user_num = int(input("positive number: "))
        if user_num <= 0:
            print("positive")
            return
        if is_prime(user_num):
            print(str(user_num) +' is prime' )
        else:
            print(str(user_num) +' is not prime' )

if __name__ == "__main__":
    main()
