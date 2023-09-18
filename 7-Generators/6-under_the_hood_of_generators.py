# how a for loop works
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            #next(iterator)
            print(next(iterator))
        except  StopIteration:
            break

special_for([1,2,3,4])

"""
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            element = next(iterator)
            print(element)
        except StopIteration:
            break
"""

def custom_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            element = next(iterator)
            # Your custom logic here
            print(element)
        except StopIteration:
            break

# Usage:
my_list = [1, 2, 3, 4, 5]
custom_for(my_list)




# how a generator (for example range) works
class MyGen():
    current = 0
    def __init__(self,first,last):
        self.first = first
        self.last = last
    def __iter__(self): 
        return self
    def __next__(self):
        if MyGen.current <self.last:
            num = MyGen.current
            MyGen.current+=1
            return num
        raise StopIteration
gen = MyGen(0,10)
for item in gen :
    print(item)
    

# recursive fib
def fib (n):
    if n==0:
        return 0
    if n==1:
        return 1

    return fib(n-2) + fib(n-1)

print(fib(8))


# non-recursive fib
def fibonacci_iterative(n):
    fib = [0, 1]  # Initialize a list to store Fibonacci numbers
    for i in range(2, n + 1):
        next_fib = fib[i - 1] + fib[i - 2]
        fib.append(next_fib)

    return fib[n]

# Usage:
n = 100000 # Replace with the desired Fibonacci number you want to calculate
result = fibonacci_iterative(n)
number_str = str(result)
length = len(number_str)
print (length)
print(f"The {n}-th Fibonacci number is {result}")

# fib with a generator
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Usage:
n = 1001  # Replace with the desired number of Fibonacci numbers you want to generate
fib_gen = fibonacci_generator(n)
for _ in range(n):
    print(next(fib_gen))
