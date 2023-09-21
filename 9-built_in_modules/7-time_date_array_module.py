import datetime
from time import time
from array import array


print(datetime.time(5,45,20))
print(datetime.date.today())

t1 = time()
print(t1)

# lists in python sometimes called array
# arrays in python takes up less memory and are faster
# if you have a large list and you dont want to use generators you can improve it with an array
# that is because when we create an array it sets how much memory we can use in our machine
"""
'b' signed char 1 byte
'B' unsigned char 1 byte
'i' signed int 2 byte
'I' unsigned int 2 byte
'f' float 4 byte
'd' double 4 byte
"""
arr = array('i', [134,3452,457093])
print(arr)
print(arr[2])
