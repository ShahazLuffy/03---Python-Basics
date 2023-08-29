print('********************************************************************************')
print('#list')
simpleList = [58, 24, 48, 69, 28, 64, 37, 26, 85, 69, 59, 51, 25, 67, 18]
print('simpleList:', simpleList)
print('********************************************************************************')
print('#reverse')
simpleListReversed = simpleList.copy()
simpleListReversed.reverse()
print('reverse of simpleList :', simpleListReversed)


print('sort simpleList:', sorted(simpleList))
#sorted does not modify the original simpleList , in addition it will also produce a value

print('********************************************************************************')
print('#sort reverse sort')

simpleListSortReverse = simpleList[:]
simpleListSortReverse.sort(reverse=True)
print('simpleListSortReverse:', simpleListSortReverse)

#slicing creates a new simpleList (produce value)
print(simpleList[: : 1])
print(simpleList[: : -1])

print('********************************************************************************')
print('#genrates a list from 1 to 9')

print(list(range(1,10)))
print('********************************************************************************')
print('#join')
listJoinOne = ' '
listJoinTwo = ['ali', 'ghaderi','pour']
print(listJoinOne.join(listJoinTwo)) #to generate a string out of list
print(' '.join(listJoinTwo))

print('********************************************************************************')
print('#list unpacking')
x, y ,z, k , *other, last= [1,2,True,'akbar lover', 234,3454,6456,567, 'this is last item']
print(k)
print('other:' , other)
print(other[1])
print(last)

person_info = [
    ("Alice", 28, "Engineer"),
    ("Bob", 35, "Data Scientist"),
    ("Carol", 42, "Manager"),
    ("David", 31, "Designer"),
]

# Process and print information using list unpacking
for name, age, occupation in person_info:
    print(f"Name: {name}, Age: {age}, Occupation: {occupation}")


print('********************************************************************************')
print('#list unpacking')



akbar = [
    ('hasan', 25, 'kerman'),
    ('reza', 32, 'ahvaz')
]

for name, age, city in akbar:
    name, age, city
print(name)