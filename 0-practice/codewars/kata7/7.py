
"""Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!"""

def get_sum(a,b):
    listo=[]
    if a==b :
        return a
    else:
        if(a>b):
            c=a
            a=b
            b=c   
        for item in range (a,b+1):
            listo.append(item)
    return sum(listo)        
print(get_sum(-2,5))


#best
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))