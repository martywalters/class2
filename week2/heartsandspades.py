# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:31:38 2024

@author: walters
"""

import random
def check_guess(random_number, user_guess):
    hearts = 0
    spades = 0
    for i in range(4):
        if user_guess[i] == random_number[i]:
            hearts += 1
        elif user_guess[i] in random_number:
            spades += 1
    return hearts, spades

def main():
    random_number = random.sample(range(10), 4)
    print("Spoiler Alert  don't look  at number: "+ str(random_number))
    guess_count = 0

    print("Hearts and Spades")
    print("input 4 digits each should be unique:")

    while True:
        input_digits = input("Your guess: ")
        try:
            user_guess = [int(digit) for digit in input_digits]
            if len(user_guess) != 4 or len(set(user_guess)) != 4:
                print("Invalid input. Enter 4 unique digits. try will not count")
                continue
        except ValueError:
            print("Invalid Input. it will not count")
            continue

        guess_count += 1
        hearts, spades = check_guess(random_number, user_guess)
        print('Hearts:'+str(hearts)+' Spades: '+str(spades))

        if hearts == 4:
            print('You guessed it in '+str(guess_count)+ ' trys')
            break

if __name__ == "__main__":
    main()
