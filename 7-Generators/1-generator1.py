# generators alloww us to generate a sequence of values over time
# one way of making a list of 1 to 100000000 is for loop which takes alot of memory
# other way (efficient way) is to use a geneartor
def make_list(num):
    return [item*2 for item in range(num)]

def make_list2(num):
    return list(range(num))
print(make_list(10))
print(make_list2(10))