"""
Short-circuiting is a concept in programming where certain boolean expressions are not fully
evaluated if the outcome can be determined early based on the value of the operands. In Python, 
    the and and or operators exhibit short-circuiting behavior.
Here's an example of short-circuiting in Python using the and operator:
"""

a = 5
b = 10

if a > 0 and b/a > 2:
    print("Both conditions are true")
else:
    print("At least one condition is false")
