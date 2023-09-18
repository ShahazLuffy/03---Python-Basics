# with map we have 3 input then we have 3 output
# in filter , we may have less output than the input
# a filter function try to receive a true or false value (boolean value) whetere it should be filtered or not
intial_list = [2,345,456,56,3,542,345,4,56,67,678,67,345,64,52,345,23,45,2456,4567,456,7,234,5,2345,1,5,246,3,456,57]
def only_odd(number):
    return number%2 !=0

print(list(filter(only_odd, intial_list)))