# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:59:45 2024

@author: walters
"""

def reverse_file_content(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
            reversed_content = content[::-1]

        with open(output_file, 'w') as outfile:
            outfile.write(reversed_content)

        print(f"Reversed content written to {output_file}")
    except FileNotFoundError:
        print(f"File '{input_file}' not found. Please provide a valid input file.")

# Example usage
input_file_name = "About_Python-1.txt"
output_file_name = "reversed_output.txt"
reverse_file_content(input_file_name, output_file_name)
