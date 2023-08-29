fruits = ['apple', 'banana', 'cherry', 'date']

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

for i, item in enumerate(range(10,15)):
    print(i, item)
    

for i, item in enumerate(list(range(10))):
    if (item==50):
        print(f"index of 5 is {i}")
