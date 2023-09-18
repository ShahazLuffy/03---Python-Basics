
def multiply_list(x):
    return x*2
print(map(multiply_list, [5,3])) # it shows the memory location
#if we want to see the result we must turn map into a list


my_list=[2,5,8]
print('map functino : ', list(map(multiply_list, my_list))) # map function is pure function it does not modify item outside it
print('original list :', my_list) 