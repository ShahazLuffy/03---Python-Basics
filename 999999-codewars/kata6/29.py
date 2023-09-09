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
print()

def digitize(n):
    k = str(n)
    ka=[]
    for item in k:
        ka.append(int(item))
    reversed_list = ka[::-1]
    
    return reversed_list
     
[8, 3, 7, 4, 6, 7, 4, 8, 9]
print(digitize(984764738))

def a1(number):
    return [int(digit) for digit in str(number)][::-1]
print(a1(1230))


def kasdf(number):
    return str(number)
print(kasdf(33434))