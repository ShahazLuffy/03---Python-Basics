"""In this simple exercise, you will build a program that takes a value, integer , and returns a list of its multiples up to another value, limit . If limit is a multiple of integer, it should be included as well. There will only ever be positive integers passed into the function, not consisting of 0. The limit will always be higher than the base.

For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.
"""
def find_multiples(integer, limit):
    if limit <integer:
        return
  
    reza = []
    akbar = int(limit / integer)
    print(akbar)
   
    if limit % integer == 0 :
        
        for item in range(akbar+1):
            print('aaa', item*integer)
            if item*integer >= integer:
                reza.append(item*integer)
    else:
       
        for item in range(akbar+1):
            print('bbb',item*integer)
            
            if item*integer >= integer:
                reza.append(item*integer)
            
    return reza

print(find_multiples(2, 3))


#best solution
def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))


#range(start, stop, step)