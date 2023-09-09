listo = "karim"
x = sorted(list(listo), reverse=True)
print(x[:2])


def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))
print(find_multiples(2,23))


print(list(range(2,14,4)))

def stringy(m):
    karim =("10"*m)[:3]
    print(type(karim))
print(stringy(3))


def square_sum(numbers):
    total = 0
    for item in numbers:
        total+=item*item
    return total
    
    
print(square_sum([1,2,11,5]))

def squaresum(numbers):
    return sum(x**2 for x in numbers)

print(squaresum([1,2,11,5]))

value1 = 2
value2 = 5
operator1='+'
print(eval("{}{}{}".format(value1, operator1, value2)))
print(eval('2+2'))
pr