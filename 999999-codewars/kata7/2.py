"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
"""
def is_isogram(stringz):
    karim = []
    for item in range(len(stringz)):
        total=0
        for kitem in range(len(stringz)):
            if stringz[item].lower() == stringz[kitem].lower():
                total +=1
                print(total)
            karim.append(total)
    for item in karim:
        if item>1:
            return False
    return True
print(is_isogram('moOse'))

#best
def is_isogram(string):
    return len(string) == len(set(string.lower()))

#best
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True