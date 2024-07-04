"""
NAME : Naganandhini M
DATE : 04-July-2024
PROGRAM : write a python program that takes string and returns most frequent character in it 
"""

# Function to count the number of words in a string
def count_words(input_string):
    # Remove leading and trailing whitespace using strip()
    input_string = input_string.strip()
    
    # Split the string into words based on whitespace
    words = input_string.split()
    
    # Return the number of words
    return len(words)

# Test the function with examples
input_string1 = "Hello, World!"
input_string2 = "    This is a test string with 8 words.   "
input_string3 = "NoSpacesHere"

# Count words in each example string
word_count1 = count_words(input_string1)
word_count2 = count_words(input_string2)
word_count3 = count_words(input_string3)

# Print the original strings and their word counts
print(f"String 1: '{input_string1}'")
print(f"Number of words: {word_count1}")

print(f"\nString 2: '{input_string2}'")
print(f"Number of words: {word_count2}")

print(f"\nString 3: '{input_string3}'")
print(f"Number of words: {word_count3}")
