# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:37:46 2024

@author: walters
"""
import datetime

def get_user_input():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    current_year = datetime.datetime.now().year
    years_to_100 = 100 - age
    year_of_100 = current_year + years_to_100
    print(f"Hello, {name}! You will turn 100 years old in the year {year_of_100}.")

def common_elements_set(a, b):
    # Convert lists to sets to find common elements
    set_a = set(a)
    set_b = set(b)
    common_set = set_a & set_b  # Intersection of sets
    z = set_b.intersection(set_a)
    print("common elements",list(z))
    return list(common_set)  # Convert back to a list

def reverse_words_list_comprehension(input_string):
    words = input_string.split()
    reversed_string = " ".join(words[::-1])
    return reversed_string

def extract_first_and_last_elements(input_list):
    # Get the first and last elements using list slicing
    result = input_list[::len(input_list) - 1]
    return result

def create_new_string(s1, s2):
    # Get the first, middle, and last characters from each input string
    new_string = s1[0]+ s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2]  + s1[-1] + s2[-1]
    return new_string



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

get_user_input()

common_elements = common_elements_set(a, b)
print("Common elements (without duplicates):", common_elements)

user_input = input("Enter a long string with multiple words: ")
reversed_result = reverse_words_list_comprehension(user_input)
print("Reversed string:", reversed_result)

a = [5, 10, 15, 20, 25]
new_list = extract_first_and_last_elements(a)
print("New list with first and last elements:", new_list)

s1 = "America"
s2 = "Japan"
result = create_new_string(s1, s2)
print("New string:", result)