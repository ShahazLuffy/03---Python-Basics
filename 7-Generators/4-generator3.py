from time import time
def performance(fn):
    def wrapper(*args,**kwargs):
        time_start = time()
        result = fn(*args, **kwargs)
        time_end = time()
        print(f'took {time_end - time_start} second')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*5


long_time()