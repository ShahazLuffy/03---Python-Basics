#data types
"""int
float
string
boolean
list
tuple
set
dic
complex
"""

#types
print(type(4.2+1.8))
print(type(3/4))
print(type(3//4))
print(type(5//4))
print(bin(3))
print(int('0b11',2))

#--------------------------------------------------------------------------------------------------------
#statement vs expression
#expression is piece of code that produce a value
#the entire line of code is a statement

iq = 100
user_age = iq/20
# iq/20 >> it produce a  value so it is an expression
#iq = 100 >> it is also a statement cause it does not produce a value, it declares a variable

#--------------------------------------------------------------------------------------------------------
#Augmented Assignment Operator
first_way = 5
first_way = first_way+2
print(first_way)

second_way = 5
second_way +=2
print(second_way)

#type converesion
print(type(int(str(5))))

#escape sequence
weather ="it's sunny"
weather_escaped = "it\'s \"kind of\" sunny"

weather_escaped_with_tab = "\tit\'s \"kind of\" sunny here"
print(weather_escaped,"\n" ,weather_escaped_with_tab)


#formatted strings
ali_name ="ali"
ali_age = 32
print(f'hi {ali_name}, you are {ali_age}')
print('hi {0} you are {1}'.format(ali_name, ali_age))

#string immutability
immutable_string = '012345'
print(immutable_string)
#immutable_string[2]='3'   >>>error
print(immutable_string+'3') #no error

#boolean
def isBool(a):
  if bool(a) == True:
    return 'bool'
  return 'not bool'
print(isBool('true'))


#list
firstList = [1,'2', True, 23,'stuff', 'False','Python', 13,'Swift', 'C++', 623, 'C', 'Java', 'akbar', 'Rust', 'R']
firstList[0]= 111
print(firstList)
newFirstList = firstList[0:2]
print(newFirstList)


#matrix
firstMatrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
print(firstMatrix[0])
print(firstMatrix[0][2]) #second element of first element of the firstMatrix
