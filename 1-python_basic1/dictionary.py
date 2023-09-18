# dictoionary is a key value data structure
# dictonary is unordered
# dictionary keys must be immutable

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "friends": ['Reza', 'Mahmood', 'Karim', "Mina"],
    True: 'khkhkh',
    123: False,
    (123, 'home'): 123456788
}

# Accessing dictionary values using keys
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])
print(my_dict["friends"])
print(my_dict[True])
print(my_dict[123])
print(my_dict[(123, 'home')])


print(my_dict.keys())
print(my_dict.values())

# .get method return value of a key if exists
print(my_dict.get('some key'))
print(my_dict.get('some key', 'intial value to prevent None'))
print(my_dict.get('friends'))

# in
print("name" in my_dict)
print("name" in my_dict.keys())

#item
print(my_dict.items())