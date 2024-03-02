# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:51:37 2024

@author: walters
"""

class Calc():

    def add(self, a, b):
        return  a + b

    def subtract(self, a, b):
        return a - b
        
    def multiply(self,a,b):
        return a * b
        
    def divide(self, a, b):
        if b==0:
            raise ValueError('Cannot divide by zero!')
        return a / b