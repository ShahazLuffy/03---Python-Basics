"""
icture =[
[0 ,0, 0, 1,0, 0 ,0],
[0 ,0, 0, 1,0, 0 ,0],
[0 ,1 ,1 ,1, 1 ,1, 0],
[0 ,1 ,1 ,1, 1 ,1, 0],
[0 ,0, 0, 1,0, 0 ,0],
[0 ,0, 0, 1,0, 0 ,0]
]


for item in picture:
    for itemx in item:
        if itemx == 1:
            print('*' , end='')
        else:
            print(' ', end='')
    print('')   
        
"""
#duplicates in a list
some_list = ['a', 'b', 'c', 'b', 'd', 'm','n','n']
holder = []
for item in some_list:
   if some_list.count(item) > 1 and item not in holder:
       holder.append(item)
    
print(holder)

#parameters vs arguments
#parameters when we define function
def say_hello (name, family):
    print(f'hello {name}  {family}')
    
#arguments when we call the function ( arguemnts are the actual value)
say_hello('ali','ghaderi')


#docstring
def test(a):
    """
    info: this function print paramtere a
    """
    print(a)

print(test.__doc__)
help(test)


#*args **kwargs
def akbar(*args, **kwargs):
    total = 0
    for item in kwargs.values():
        total+=item
    return sum(args) + total
print(akbar(2,4,5, num1=5, num2 = 6))

# kwargs is a set


def hieghst_even(a):
    j=[]
    for item in a:
        if item % 2 ==0 :
            j.append(item)
    return max(j)
print(hieghst_even([55,66,77,4,5,6]))