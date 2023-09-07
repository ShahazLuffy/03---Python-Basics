def reverse_seq(n):
    akbar=[]
    for item in range(n+1):
        akbar.append(item)
    akbar.remove(0)
    return akbar[::-1]
print(reverse_seq(5))

#best
def reverseseq2(n):
    return list(range(n, 0, -1))