# decorator syntax
def my_decorator(func):
    def wrap_func(greeting):
        print('before calling function')
        func(greeting)
        print('after calling function')     
    return wrap_func


# example 1
@my_decorator
def hello(greeting): # if this function takes argument we need to take argument in wrap_function too, since we dont know how many arguments our hello function may have we use *args and **kwargs
    print(greeting)

hello('salam')

akbar = my_decorator(hello)
akbar('hello')

print('--------------------------------------- *args and **kwargs')
#decorator patter
def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print('before calling function')
        func(*args, **kwargs)
        print('after calling function')     
    return wrap_func


# example 1
@my_decorator2
def hello(greeting): # if this function takes argument we need to take argument in wrap_function too, since we dont know how many arguments our hello function may have we use *args and **kwargs
    print(greeting)

hello('salam')

akbar = my_decorator(hello)
akbar('hello')