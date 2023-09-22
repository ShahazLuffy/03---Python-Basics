my_file = open('a.txt')
print(my_file.read()) # you can read a file once
#cause the curser is at end of the line
# with seek we move curser whereever we want

print(my_file.read())
print(my_file.read())
print(my_file.read())
my_file.seek(0) #move curse to positon 0
print(my_file.read())
my_file.seek(1) #move curse to positon 0


print(my_file.readline())
print(my_file.readline())
print(my_file.readlines()) # a list with entire file

my_file.close()
