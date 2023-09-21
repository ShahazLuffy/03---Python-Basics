import random
import string
from collections import Counter, defaultdict, OrderedDict

print('-------------------------Counter-----------------------------')
li = []
for item in range(20):
    li.append(random.randint(1, 10))
print(Counter(li))  # total occurrence item in an iterable

random_string = ''.join(random.choice(string.ascii_letters) for _ in range(50))
print(random_string)
print(Counter(random_string))

print('-------------------------defaultdict-----------------------------')
dictonary = {'a': 1, 'b': 2}
print(dictonary['a'])
try:
    print(dictonary['c'])
except KeyError:
    print('KeyError, use defaultdict')

default_dictionary = defaultdict(int, {'a': 1, 'b': 2})  # the first parameter is a calllable
print(default_dictionary['c'])
print(int())  # we get 0 because of this

default_dictionary2 = defaultdict(lambda: 5, {'a': 1, 'b': 2})  # the first parameter is a calllable
print(default_dictionary2['c'])

default_dictionary3 = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})  # the first parameter is a calllable
print(default_dictionary3['c'])

print('-------------------------OrderedDict-----------------------------')
# remember a regular dictionary has no order
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

d3 = OrderedDict()
d3['b'] = 2
d3['a'] = 1

print(d1 == d2)
print(d3 == d2)

# a regular dict
d4 = {'a': 1, 'b': 2}
d5 = {'b': 2, 'a': 1}
print(d4 == d5)
