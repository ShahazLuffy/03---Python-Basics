"""
a pure function has two rules
one is that given the same input it will always return same output

a function should not produce any side effects
a side affect is like imaging you have a printing function and everytime u run the function you change the value of a variable which is being used outside of this function

pure function = less buggy code + cleaner code + debugging is easier
"""

# pure function
def multiply_list(listo):
    return [x*2 for x in listo]

print(multiply_list([1,3,5]))

# not pure function
new_list = []
def multiply_list2(listo):
    
    for item in listo:
       new_list.append(item)
    return print(new_list)  # this print is a side effect (it effects sth outside this function)


new_list = ''
print(multiply_list2([3,45,3]))