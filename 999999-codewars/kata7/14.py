import os

# Create a new directory
os.makedirs('D:/Ali Ghaderipour/workplace/Python/03 - Python Basics/999999-codewars/kata5')

# Create files inside the directory
for i in [1,3,5]:
    open(f'D:/Ali Ghaderipour/workplace/Python/03 - Python Basics/999999-codewars/kata5/{str(i)}.py', 'w').close()