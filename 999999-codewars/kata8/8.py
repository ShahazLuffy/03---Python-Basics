def digitize(n):
    k = str(n)
    ka=[]
    for item in k:
        ka.append(int(item))
    reversed_list = ka[::-1]
    
    return reversed_list
     
print(digitize(984764738))


#best
def digitize2(n):
    return map(int, str(n)[::-1])