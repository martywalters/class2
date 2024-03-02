# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:02:52 2024

@author: walters
"""
# test_calc.py

import unittest
from calc import add, subtract, multiply, divide

class TestCalcFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(1, 1), 1)
        with self.assertRaises(ValueError):
            divide(5, 0)  # Should raise ValueError for division by zero

if __name__ == '__main__':
    unittest.main()

