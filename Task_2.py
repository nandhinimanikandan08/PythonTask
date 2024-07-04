"""
NAME : Naganandhini M
DATE : 04-July-2024
PROGRAM : write a python program to create pyramid of numbers from 1 to 20 using for loop?

"""




# number of levels for the pyramid
num_of_levels = 20

# Outer loop to iterate through each level of the pyramid
for i in range(1, num_of_levels + 1):
    # Inner loop to print numbers in each level
    for j in range(1, i + 1):
        # Print the number followed by a space (end=' ' ensures numbers are printed on the same line)
        print(j, end=' ')
    # Move to the next line after each level is printed
    print()
