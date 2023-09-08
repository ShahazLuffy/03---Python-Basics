#mask all string except last 4 character
# return masked string
def maskify(cc):
    listo = list(cc)
    for item in range(len(listo)-4):
        listo[item] = '#'
    return ''.join(listo)
print(maskify('SF$SDfgsd2eA'))