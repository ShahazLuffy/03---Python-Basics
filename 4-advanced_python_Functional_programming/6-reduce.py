from functools import reduce
def accumulator(acc, item):
    return acc+ item

my_list = [2,345,456,56,3,542,345,4,56,67,678,67,345,64,52,345,23,45,2456,4567,456,7,234,5,2345,1,5,246,3,456,57]
print(reduce(accumulator,my_list,0)) 
print(sum(my_list))

print('--------------------------------------------------------------------------------------')



# Example 2: Finding the Maximum Value in a List
numbers = [10, 5, 8, 20, 3]
max_result = reduce(lambda x, y: x if x > y else y, numbers)
print(max_result)  # Output: 20

# Example 3: Concatenating Strings
words = ["Hello", " ", "world", "!"]
concatenated_string = reduce(lambda x, y: x + y, words)
print(concatenated_string)  # Output: "Hello world!"

# Example 4: Product of All Elements in a List
numbers = [2, 3, 4, 5]
product_result = reduce(lambda x, y: x * y, numbers)
print(product_result)  # Output: 120 (2*3*4*5)

# Example 5: Factorial Calculation
n = 555555
factorial = reduce(lambda x, y: x * y, range(1, n+1))
print(factorial)  # Output: 120 (5! = 5*4*3*2*1)
