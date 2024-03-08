# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:50:22 2024

@author: walters
"""

class StringModify:
    def __init__(self):
        self.user_string = ""

    def get_String(self):
        self.user_string = input("Enter a string: ")

    def print_String(self):
        print(self.user_string.upper())

