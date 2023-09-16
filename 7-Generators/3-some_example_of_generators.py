"""Generators in Python are a way to create iterators. They allow you to generate values lazily, one at a time, instead of generating all the values at once and storing them in memory. This can be very useful for working with large datasets or when you want to avoid unnecessary memory consumption.

Here are some practical examples of using generators in functions:
"""
# 1-Counting Numbers Generator:
# this generator function yields numbers from 1 to n one at a time.
def count_numbers(n):
    for i in range(1, n + 1):
        yield i

# Usage:
for num in count_numbers(5):
    print(num)


# Fibonacci Sequence Generator:
# This generator function generates the first n Fibonacci numbers.
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Usage:
for num in fibonacci(10):
    print(num)


# File Line Reader Generator:
# This generator reads lines from a file one at a time, eliminating the need to load the entire file into memory.
def read_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# Usage:
for line in read_lines('example.txt'):
    print(line)

# Infinite Generator:
# This generator generates an infinite sequence of numbers starting from the given value.
def infinite_counter(start=0):
    while True:
        yield start
        start += 1

# Usage:
counter = infinite_counter()
for _ in range(5):
    print(next(counter))


# Generator Expression:
# Generator expressions are a concise way to create generators. They are similar to list comprehensions but use parentheses instead of square brackets.
squares = (x**2 for x in range(1, 6))
for square in squares:
    print(square)

# This generator expression yields the squares of numbers from 1 to 5.

# Generators are memory-efficient and allow you to work with large datasets or infinite sequences without consuming excessive memory. They are a fundamental tool for Python developers when dealing with streaming data or when you need to generate values on the fly.