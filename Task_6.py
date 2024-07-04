"""
NAME : Naganandhini M
DATE : 04-July-2024
PROGRAM : write a python program that takes string and returns most frequent character in it 
"""

def most_frequent_character(input_string):
    # Initialize an empty dictionary to count occurrences of each character
    char_count = {}
    
    # Count occurrences of each character in the input string
    for char in input_string:
        if char in char_count:
            char_count[char] += 1  # Increment count if character already exists in dictionary
        else:
            char_count[char] = 1   # Initialize count to 1 if character doesn't exist in dictionary
    
    # Initialize variables to track the most frequent character and its count
    max_char = ''
    max_count = 0
    
    # Iterate through the dictionary to find the most frequent character
    for char, count in char_count.items():
        if count > max_count:
            max_char = char
            max_count = count
    
    # Return the most frequent character
    return max_char

# Test the function with an example string
input_string = "Finally got something"
most_frequent_char = most_frequent_character(input_string)

# Print the original string and the most frequent character
print("Original string:", input_string)
print("Most frequent character:", most_frequent_char)
