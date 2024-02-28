# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:25:34 2024

@author: walters
"""

import random

def main():
    # random number:   number = random.randint(MINIMUM, MAXIMUM)
    number = random.randint(0, 100)
    

    win = False
    guess_count  = 0
    
    # while not a winner
    while not win:
        # enter guess
        userNum = int(input("Please guess a number between 0 and 100: "))
        
        # Check number
        if userNum > number:
            message = "Too high, try again."
            guess_count += 1
        elif userNum == number:
            message = "correct!"
            guess_count += 1
            win = True
        else:
            message = "Too low, try again."
            guess_count += 1
        
        print()
        print(message)

    print()
    print("Total guesses:",  guess_count)

if __name__ == "__main__":
    main()
