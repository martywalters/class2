# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:22:01 2024

@author: walters
"""
print("Part1.")
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
even_elements = [x for x in a if x % 2 == 0]
print(even_elements)

print("Part2.")
import guess
guess.main()

print("Part3.")
import heartsandspades
heartsandspades.main()

print("Part4.")
import fibonacci
fibonacci.main()

print("Part5.")
import prime
prime.main()
