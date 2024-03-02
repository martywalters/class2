# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:52:33 2024

@author: walters
"""
import calcClass as calc
class ModulusCalc(calc.Calc):
    def modulus_divide(self, a, b):
        if b == 0:
            raise ValueError('Cannot divide by zero!')
        return a % b

# Create an object of the child class
calc_obj = ModulusCalc()

# Test the functions
print("Addition:", calc_obj.add(10, 5))
print("Subtraction:", calc_obj.subtract(10, 5))
print("Multiplication:", calc_obj.multiply(10, 5))
print("Division:", calc_obj.divide(10, 5))
print("Modulus Division:", calc_obj.modulus_divide(10, 5))
