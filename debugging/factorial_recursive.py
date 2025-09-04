#!/usr/bin/python3
import sys

# Define a recursive function to calculate factorial.
# Factorial is defined as:
#   n! = n × (n-1) × (n-2) × ... × 1
# Special case: 0! = 1
def factorial(n):
    if n == 0:
        return 1   # Base case: stop recursion
    else:
        return n * factorial(n-1)  # Recursive step

# Read the first command-line argument, convert it to int,
# and calculate its factorial.
# Note: this will crash if no argument is provided or if the input isn't an integer.
f = factorial(int(sys.argv[1]))

# Print the result to standard output
print(f)
