# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:35:52 2024

@author: walters
"""

"""
There are many more methods for String handling in Python than the ones seen in this lecture. Research and give an example for:
string searching
modifying
filling,
splitting
and joining.  
"""
txt = "Hello, welcome to my world."
index_of_welcome = txt.find("welcome")
print("Index of 'welcome':", index_of_welcome)
index_of_not_welcome = txt.find("NOT")
print("Index of Not found:", index_of_not_welcome)
print(index_of_welcome != -1)
print(index_of_not_welcome != -1 )

original_string = "Hello, World!"
uppercase_string = original_string.upper()
print("Uppercase:", uppercase_string)

original_string = "Hello, World!"
lowercase_string = original_string.lower()
print("Lowercase:", lowercase_string)

original_string = " Hello, World! "
trimmed_string = original_string.strip()
print("Trimmed:", trimmed_string)

original_string = "Hello, World!"
new_string = original_string.replace("H", "J")
print("Replaced:", new_string)

original_string = "Hello, World!"
split_list = original_string.split(",")
print("Split list:", split_list)  # Output: ['Hello', ' World!']

original_string = "Hi"
left_padded = original_string.ljust(10)
right_padded = original_string.rjust(10)
print("Left-padded:", left_padded)  # Output: 'Hi         '
print("Right-padded:", right_padded)  # Output: '         Hi''

txt = "50"
zero_padded = txt.zfill(10)
print("Zero-padded:", zero_padded)  # Output: '0000000050'
