if True:
    x = 10
print(x)


def akbar(reza):
    y = 10
# print(y)


a = 1


def confusion():
    a = 5
    return a


print(a)
print(confusion())

print('*****************')
print(confusion())
print(a)


# scope order rule
# 1- start with local scope
# 2- parent local scope (if not in local scope)
# 3- global scope
# 4- built in function

b = 42


def confusion2():
    return b


print(confusion2())
print(b)


c = 25


def confusion3():
    c = 9.24

    def confusion4():
        return c
    return confusion4()


print(c)
print(confusion3())

d = 91


def confusion5():
    z = 9.24

    def confusion6():
        return d
    return confusion6()


print(d)
print(confusion5())
