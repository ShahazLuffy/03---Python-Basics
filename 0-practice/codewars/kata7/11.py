def printer_error(s):
    a=0
    for item in s:
        if item >='n':
            a+=1
    return "{}/{}".format(4, len(s)) 

print(printer_error("aaabbbbhaijjjm"))

#best
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))