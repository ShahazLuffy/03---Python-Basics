# decorator syntax
def my_decorator(func):
    def wrap_func():
        print('before calling function')
        func()
        print('after calling function')     
    return wrap_func


# example 1
@my_decorator
def hello():
    print('hello')
hello()



# example 2
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_args
def add(a, b):
    return a + b

result = add(3, 5)



# example 3
import time
def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to run")
        return result
    return wrapper

@timing
def slow_function():
    time.sleep(2)

slow_function()


# example 4
def authenticate(func):
    def wrapper(user):
        if user.is_authenticated:
            result = func(user)
        else:
            result = "Access denied. Please log in."
        return result
    return wrapper

@authenticate
def protected_route(user):
    return f"Welcome, {user.name}!"

class User:
    def __init__(self, name, is_authenticated):
        self.name = name
        self.is_authenticated = is_authenticated

user1 = User("Alice", True)
user2 = User("Bob", False)

print(protected_route(user1))  # Output: "Welcome, Alice!"
print(protected_route(user2))  # Output: "Access denied. Please log in."


