"""
NAME : Naganandhini M
DATE : 04-July-2024
PROGRAM : write a python program takes a string and returns a new string with all vowels removed

"""

# Creating  Function to remove vowels from a string
def remove_vowels(input_string):
    # Define vowels as a string of all lowercase and uppercase vowels
    vowels = "aeiouAEIOU"
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is not a vowel
        if char not in vowels:
            # Append the character to the result string
            result += char
    
    # Return the result string without vowels
    return result

# Testing the function with an example string
input_string = "Hai , I am testing this sentence to remove vowels from it "
output_string = remove_vowels(input_string)

# Printing the original and modified strings
print("Original string:", input_string)
print("String without vowels:", output_string)
