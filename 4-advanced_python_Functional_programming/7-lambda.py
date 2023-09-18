"""
Lambda functions in Python, often referred to as "lambda expressions," are a way to create small, anonymous functions. They are called "anonymous" because they don't have a name like regular functions defined with the def keyword. Instead, lambda functions are defined using the lambda keyword, followed by a list of arguments, a colon (:), and an expression. The result of the lambda expression is a function that can be assigned to a variable or used as an argument to other functions.

Lambda functions are typically used for short, simple operations, and they can be a convenient way to create functions on the fly, especially when you need a small function for a specific task. Here are some key points about lambda functions:

   1. Anonymous Functions: Lambda functions do not have a name. They are defined and used in one line of code.

   2. Single Expression: Lambda functions can only contain a single expression. The value of this expression is returned when the lambda function is called.

   3. Limited Use Cases: Lambda functions are best suited for simple operations and are not intended to replace regular functions for more complex tasks.

   4. No Statements: Lambda functions cannot contain statements or multiple expressions. They are limited to a single expression that is evaluated and returned.

   5. Functional Programming: Lambda functions are often used in functional programming paradigms, where functions are treated as first-class citizens and can be passed as arguments to other functions.
"""
# lambda param: action on param
# lambda is anonymous function >> they only being used once and have no name



# Example 1: A lambda function that adds two numbers
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8

# Example 2: Using lambda with built-in functions like sorted
points = [(1, 2), (3, 1), (0, 0), (2, 2)]
sorted_points = sorted(points, key=lambda point: point[0])
print(sorted_points)  # Output: [(0, 0), (1, 2), (2, 2), (3, 1)]

# Example 3: Lambda function as an argument to filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


print('-----------------------filter + lambda function--------------------------------------------')

from functools import reduce
print(list(map(lambda item: item*2, [1,2,3,4])))
print(list(filter(lambda item:item%2 !=0 ,(map(lambda item: item+3, [1,2,3,4]))))) # item of list + 3 and then check which one is odd
product_result = reduce(lambda x, y: x * y, list(filter(lambda item:item%2 !=0 ,(map(lambda item: item+3, [1,2,3,4])))))
print(product_result)

# square 2
print(list(map(lambda item:item**2, [2,5,6])))

# sort based on second item in tuple
list_need_to_be_sorted = [(0,2), (4,3), (10,-1),(9,9)]

list_need_to_be_sorted.sort(key= lambda x:x[1])
print(list_need_to_be_sorted)
