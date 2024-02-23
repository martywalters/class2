# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:37:46 2024

@author: walters
"""
#Part 1.
import datetime
def user_input_name_age():
    name = input("name: ")
    age = int(input("Age: "))
    curr_year = datetime.datetime.now().year
    to_100 = 100 - age
    year_100 = curr_year + to_100
    print(name + " you will turn 100 in the year "+ str(year_100))
 
#Part 2.
def common_elements(a, b):
    set_a = set(a)
    set_b = set(b)
   #zcommon_set = set_a & set_b 
    z = set_b.intersection(set_a)
    return list(z)  # Convert back to a list

#Part 3.
def backwards_order(input_string):
    words = input_string.split()
    reversed = " ".join(words[::-1])
    return reversed

#Part 4
def extract_first_last(in_list):
    short_list = in_list[::len(in_list) - 1]
    return short_list
#Part 5
def create_string(s1, s2):
    new_str = s1[0]+ s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2]  + s1[-1] + s2[-1]
    return new_str




# Part 1.   Get name and age display message of name 
# and age they will turn 100
user_input_name_age()

# Part 2. 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_elements = common_elements(a, b)
print("Common between the list  (without duplicates):", common_elements)

# Part 3.
instring = input("Enter long string containing multiple words: ")
reversed_str = backwards_order(instring)
print("String reversed:", reversed_str)

#Part 4
a = [5, 10, 15, 20, 25]
short_list = extract_first_last(a)
print("First Last :", short_list)

#Part 5
s1 = "America"
s2 = "Japan"
result = create_string(s1, s2)
print("Modified String:", result)