import os

# Create a new directory
os.makedirs('D:/Ali Ghaderipour/workplace/Python/03 - Python Basics/999999-codewars/kata72')

# Create files inside the directory
for i in range(3, 15):
    open(f'D:/Ali Ghaderipour/workplace/Python/03 - Python Basics/999999-codewars/kata72/{str(i)}.py', 'w').close()