simple_dict = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
my_dict = {key:value +5 for key,value in simple_dict.items() if value %2 ==0}
print(my_dict)


# all comprehensive exercise
some_list= ['a', 'b', 'c','b','d', 'm', 'n','n']
print(set([char for char in some_list if some_list.count(char)>1]))
