"""first letter of each word into capital

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

"""
def to_jaden_case(string):
    listString = string.split()
    return ' '.join([x.capitalize() for x in listString])


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

#best
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())