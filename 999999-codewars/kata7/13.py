import os
import shutil

# Define the directory path where the file is located
directory = 'D:/Ali Ghaderipour/workplace/Python/03 - Python Basics/999999-codewars/aaaa'

# Define the name of the file to be renamed and copied
filename = '1.jpg'

# Rename the file to 1.jpg
os.rename(os.path.join(directory, filename), os.path.join(directory, '1.jpg'))

# Create copies of the file renamed to 2.jpg, 3.jpg, and 4.jpg
for i in [33,55]:
    shutil.copy(os.path.join(directory, '1.jpg'), os.path.join(directory, f'{i+2}.jpg'))