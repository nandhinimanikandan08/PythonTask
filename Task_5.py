"""
NAME : Naganandhini M
DATE : 04-July-2024
PROGRAM : write a python program that takes string and return true value if it is a palindrome , False otherwise
"""
 

# Function to check if a string is a palindrome
def is_palindrome(input_string):
    # Convert the input string to lowercase and remove spaces
    processed_string = input_string.lower().replace(" ", "")
    
    # Reverse the processed string
    reversed_string = processed_string[::-1]
    
    # Check if the processed string is equal to its reverse
    return processed_string == reversed_string

# Test the function with examples
input_string1 = "A man a plan a canal Panama"
input_string2 = "hello"

# Check if input_string1 is a palindrome
result1 = is_palindrome(input_string1)
print(f"Is '{input_string1}' a palindrome? {result1}")

# Check if input_string2 is a palindrome
result2 = is_palindrome(input_string2)
print(f"Is '{input_string2}' a palindrome? {result2}")
