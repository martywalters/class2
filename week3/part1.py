# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:50:22 2024

@author: walters
"""
#The class should have a constructor that returns the string
#entered by the user as an argument.
#
class StringModify:

    def __new__(cls,user_string):
        instance = super().__new__(cls)

        # Set the value as an attribute
        instance.value = user_string
        return instance
    
    def __init__(self,user_string):
        self.user_string = user_string

    def get_String(self):
        return self.user_string

    def print_String(self):
        print(self.get_String().upper())
        #print(self.user_string.upper())

