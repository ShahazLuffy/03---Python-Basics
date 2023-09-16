# an iterable has __iter__ method
# generators are actually iterable
# but not everything is iterable is a generator
# a generator is a subset of an iterable
# the difference between a generator and a regular iterable is the way we implement them

# this make_list function takes alot of space in memory
def make_list(num):
    result = []
    for item in range(num):
        result.append(item)
    return result


# yield paused the function and comes back to it when we do something to i, which is called next
def generator_function(num):
    for i in range(num):
        yield i
        
        
        
my_list = make_list(10)
print(my_list)

for item in generator_function(20): # only 1 item in memory (print(item)) command
    print(item)
    
    
g = generator_function(100)
next(g) # yield pause thefunction and comes back to it when next(g) is called
next(g)
next(g)
next(g)
print('next(g) is : ',next(g))