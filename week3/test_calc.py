# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:02:52 2024

@author: walters
"""

import unittest
from calc import add, subtract, multiply, divide

class TestCalcFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ValueError):
            divide(1,0)  

if __name__ == '__main__':
    unittest.main()
    
    
