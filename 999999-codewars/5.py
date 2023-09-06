""""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 12+22+22=91^2 + 2^2 + 2^2 = 912+22+22=9.
"""
def square_sum(numbers):
    total = 0
    for item in numbers:
        total+=item*item
    return total
    
    
print(square_sum([1,2,11,5]))

#best answer
def square_sum2(numbers):
    return sum(x ** 2 for x in numbers)