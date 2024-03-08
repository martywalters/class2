# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:52:33 2024

@author: walters
"""
import calcClass as calc
class modCalc(calc.Calc):
    def modulus_divide(self, a, b):
        if b == 0:
            raise ValueError('divide by zero')
        return a % b
