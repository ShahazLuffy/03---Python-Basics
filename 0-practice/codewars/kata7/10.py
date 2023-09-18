def find_next_square(sq):
    return int(((sq**0.5)+1)) ** 2 if float(int(sq**0.5)) == sq**0.5 else -1
    
print(find_next_square(121))

sq = 121
a= int(sq**0.5)
b=sq**0.5
print(a, b)