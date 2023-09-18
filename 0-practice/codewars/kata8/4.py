"""
write me a function stringy that takes a size and returns a string of alternating 1s and 0s.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.
"""
def stringy(size):
   listo = []
   for item in range(1, size+1):
       listo.append("0") if item%2==0 else listo.append("1")
   return "".join(listo)

print(stringy(3))

#best solution
def stringy2(size):
    return ('10' * size)[:size]
print(stringy2(2))

