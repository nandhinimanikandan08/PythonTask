"""
NAME : Naganandhini M
DATE : 04-July-2024
PROGRAM : write a python program takes a string and returns a new string with all vowels removed
"""

# Creating Function to count unique characters in a string
def count_unique_characters(input_string):
    # Initialize an empty set to store unique characters
    unique_chars = set()
    
    # Iterate through each character in the input string
    for char in input_string:
        # Add the character to the set (sets automatically handle duplicates)
        unique_chars.add(char)
    
    # Return the number of unique characters
    return len(unique_chars)

# Test the function with an example string
input_string = "I am new to python programming"
unique_count = count_unique_characters(input_string)

# Print the original string and the count of unique characters
print("Original string:", input_string)
print("Number of unique characters:", unique_count)
 