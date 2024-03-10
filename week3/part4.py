# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:56:56 2024

@author: walters
"""

def count_lines_and_words():
    num_lines = 0
    num_words = 0
    filename = 'About_Python-1.txt'


    with open(filename, 'r') as file:
        for line in file:
            num_lines += 1
            words = line.split()  # Split line into words
            num_words += len(words)  # Count the words in the line

    print(f"Number of lines in '{filename}': {num_lines}")
    print(f"Total number of words in '{filename}': {num_words}")



