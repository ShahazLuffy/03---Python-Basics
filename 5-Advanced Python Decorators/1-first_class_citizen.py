"""
in python, functions are what we call first class citizens.
they can be passed around like variables
they can be an argument inside a function
they can act just like a variable

"""
def hello():
    return 'hello'

greet = hello()
print(greet)

greet2 = hello
del hello # hello function name got deleted but the function is still inside the memory and the greet is still poitning to it so print(greet) still works
print(greet2)



#functions can be passed as arguments to another function
def print_red():
    print('this is a red color')
def say_hello(func):
    func()

say_hello(print_red)

#another example
from functools import reduce
intial_list = list(range(10))

def instial_func(random_list):
    return list(filter(lambda x: x % 2 == 0, intial_list))

def second_funct(functuin):
    return list(map(lambda x : x+100, functuin))

print(second_funct(instial_func(intial_list)))


#decorators supercharge our functions
