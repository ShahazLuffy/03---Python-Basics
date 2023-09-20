import random
print(random)
help(random)
print(dir(random))

print(random.random()) #a random number between 0 and 1
print(random.randint(1,10)) #a random number between 1 and 10
print(random.choice([1,2,3,4,5,6,7,8])) # random from this list I provided
shuffle_list = [1,2,3,4,5,6,7,8]
random.shuffle(shuffle_list)
print(shuffle_list) #shuffles the list
