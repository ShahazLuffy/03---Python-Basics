"""
In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

The result should also be ordered from highest to lowest.

Examples:

[4, 10, 10, 9]  =>  [10, 9]
[1, 1, 1]  =>  [1]
[]  =>  []

"""

#my answer
def two_highest(arg1):
    akbar = set(arg1)
    aaa = sorted(akbar, reverse=True)
    if len(aaa) >2 :
        return aaa[0:2]
    else:
        return aaa


print(two_highest([15, 20, 20, 17]))

#best answer
def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]
   


