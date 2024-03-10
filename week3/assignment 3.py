print('***Part 1***')
from part1 import StringModify

user_string = StringModify("this is a test string")

#String entered by the user as an argument "value".
print(user_string.value)
user_string.print_String()
print()
print('***Part 2***')
# Create an object of the child class
from part2 import modCalc
calc_obj = modCalc()

# Test functions
print("Addition:", calc_obj.add(12, 8))
print("Subtraction:", calc_obj.subtract(18, 8))
print("Multiplication:", calc_obj.multiply(10, 2))
print("Division:", calc_obj.divide(20, 5))
print("Modulus Division:", calc_obj.modulus_divide(10, 6))
print()
print('***Part 3*** ')
#see  test_calc.py and calc.py
print('See Part 3 below : test_calc.py and calc.py')
print()
print('***Part 4***')
import part4
part4.count_lines_and_words()
print()
print('***Part 5***')
import part5
input_file_name = "About_Python-1.txt"
output_file_name = "reversed_output.txt"
part5.reverse_file_content(input_file_name, output_file_name)
