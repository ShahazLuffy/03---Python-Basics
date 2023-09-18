# 1.Generating a Sequence of Numbers:
# You can use a generator to create a sequence of numbers lazily:
# This generator function yields numbers from 0 to n-1.
def number_generator(n):
    for i in range(n):
        yield i

# Usage:
for num in number_generator(5):
    print(num)


# 2.Reading Large Files Line by Line:
# Generators are great for reading large files line by line without loading the entire file into memory:
# This generator reads lines from a file one at a time, making it memory-efficient.
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# Usage:
for line in read_large_file('large_file.txt'):
    #process_line(line)
    print(line, end='') 


# 3.Infinite Sequences:
# Generators are ideal for generating infinite sequences like an infinite counter:
# This generator produces an infinite sequence of numbers.
def infinite_counter(start=0):
    while True:
        yield start
        start += 1

# Usage:
counter = infinite_counter()
for _ in range(5):
    print(next(counter))


# 4.Filtering Data with a Generator Expression:
# You can use generator expressions to filter and process data lazily:
# This generator expression yields even numbers from the list data.
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = (x for x in data if x % 2 == 0)
for num in even_numbers:
    print(num)


# 5.Fibonacci Sequence Generator:
# Creating a generator for generating the Fibonacci sequence:
# This generator produces an infinite Fibonacci sequence.

    def fibonacci_sequence():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    # Usage:
    fib_gen = fibonacci_sequence()
    for _ in range(10):
        print(next(fib_gen))


# Generators are incredibly useful for tasks that involve processing large amounts of data, working with streams, or when you need to generate values on the fly without consuming excessive memory. They are a key feature in Python for creating efficient and memory-friendly code.
