"""
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
Numerical Score 	Letter Grade
90 <= score <= 100 	'A'
80 <= score < 90 	'B'
70 <= score < 80 	'C'
60 <= score < 70 	'D'
0 <= score < 60 	'F'

Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100."""


def get_grade(s1, s2, s3):
    score = (s1+s2+s3)/3
    print(score)
    if int(score) in range(90, 101):
        return 'A'
    if int(score) in range(80, 91):
        return 'B'
    if int(score) in range(70, 81):
        return 'C'
    if int(score) in range(60, 71):
        return 'D'
    if int(score) in range(0, 61):
        return 'F'



print(get_grade(95, 90, 93))

#best
def get_grade2(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"
    
    
    
def get_grade3(*s):
    return 'FFFFFFDCBAA'[sum(s)//30]