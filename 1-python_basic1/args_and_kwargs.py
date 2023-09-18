def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

product = multiply(2, 3, 4, 5)
print(product)  # Output: 120 (2 * 3 * 4 * 5)


def greet(**kwargs):
    greeting = kwargs.get('greeting', 'Hello') #.get(if exists, it did not exist)
    name = kwargs.get('name', 'Guest')
    return f"{greeting}, {name}!"

message1 = greet()
message2 = greet(greeting='Hi', name='Alice')
print(message1)  # Output: "Hello, Guest!"
print(message2)  # Output: "Hi, Alice!"


def print_info(name, **kwargs):
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info('Alice', age=30, city='New York')
# Output:
# Name: Alice
# age: 30
# city: New York
