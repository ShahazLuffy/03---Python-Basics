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
    print('long_time1')
    for i in range(1000000000): # range is a generator
        i*5

@performance
def long_time2():
    print('long_time2')
    for i in list(range(1000000000)): # list is not a generator
        i*5


long_time()

long_time2()

# generators are so much faster than lists