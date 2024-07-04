"""
NAME : Naganandhini M
DATE : 04-July-2024
PROGRAM : write a python program that takes string and returns most frequent character in it 
"""

# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if lengths of both strings are equal
    if len(str1) != len(str2):
        return False
    
    # Sort both strings and compare
    return sorted(str1) == sorted(str2)

# Test the function with examples
input_str1 = "Listens"
input_str2 = "Silent"
result = are_anagrams(input_str1, input_str2)

# Print the original strings and the result
print(f"String 1: '{input_str1}'")
print(f"String 2: '{input_str2}'")
print(f"Are they anagrams? {result}")
