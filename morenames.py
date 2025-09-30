# names.py
# CSIS-110 Fall 2025
# Ira Goldstein

# Simple loop using range()

# A function to print a series of names.
# It does not have any parameters
def printNames():
  first_names = ["Drake", "Taylor", "Chappell"]
  last_names = ["Graham", "Swift", "Roan"]
  for first in first_names:
    for last in last_names:
        print(first, last)

# Call our function
printNames()
