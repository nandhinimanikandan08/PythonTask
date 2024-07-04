"""
NAME : Naganandhini M
DATE : 04-July-2024
PROGRAM : write a python program to calculate total number of vowels and count of each
 vowels A,E,I,O,U in the string ' Guvi geeks Network private limited' ?

"""

#  input
input_string = 'Guvi geeks Network private limited'

# Converting  the input string to lowercase to make the counting case-insensitive
input_string_lower = input_string.lower()

# Initialize variables to count total vowels and individual vowels
total_vowels = 0
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# Defining a set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Iterate through each character in the string
for char in input_string_lower:
    # To Check if the character is a vowel
    if char in vowels:
        # Increment the total vowel count
        total_vowels += 1
        # Increment the count of the specific vowel
        if char == 'a':
            count_a += 1
        elif char == 'e':
            count_e += 1
        elif char == 'i':
            count_i += 1
        elif char == 'o':
            count_o += 1
        elif char == 'u':
            count_u += 1

# Printing  the results
print(f"Total number of vowels: {total_vowels}")
print(f"Number of 'A' vowels: {count_a}")
print(f"Number of 'E' vowels: {count_e}")
print(f"Number of 'I' vowels: {count_i}")
print(f"Number of 'O' vowels: {count_o}")
print(f"Number of 'U' vowels: {count_u}")
