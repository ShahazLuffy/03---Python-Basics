# set
my_set = {1, 2, 2, 2, 2, 4, 5}
my_set.add(2)
my_set.add(552)
print(my_set)

duplicated_list = [58, 58, 24, 24, 24, 24, 24, 24, 24, 48,
                   69, 28, 64, 37, 18, 26, 85, 69, 59, 51, 25, 67, 18]
print(set(duplicated_list))  # set has no duplicate value
no_duplicated_set = set(duplicated_list)
print(67 in no_duplicated_set)

# asfasdfasdfasdfasdf
print('test commit')

print('**********************************************************************')
print('set metods')
#set methods
# .difference()
# .difference_update()
# .intersection()
# .intersection_update()
# .discard
# .issubset()
# .isupperset()
#. union()

setA = {1,3,5,7,9,0,100}
setB = {2,4,6,8,0,1}
setA.difference(setB)
"""
print(setA)
print(setA.difference_update(setB))
print(setA.intersection(setB))
setA.discard(100)
print(setA)

"""





