class PlayerCharacter: 
    membership = True 
# we learned that we can have attribute for a class 
# but what about a method? we want method for class
    def __init__(self, name, age): 
        
        if(age > 18):
            self.name = name
            self.age = age
    def shout(self): 
        print(f'my name is {self.name}') 
    
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2
    @classmethod
    def instanciate_classmethod(cls,num1, num2):
        return cls('teddy', num1+num2)
    @staticmethod # same as classmethod except no access to cls
    def test():
        pass
    
player1 = PlayerCharacter('Tom' , 20)
print(player1.adding_things(2,3))

# we do not need to instanciate when we need class method
print(PlayerCharacter.adding_things(4,5))

# we can use cls to instanciate
player3 = PlayerCharacter.instanciate_classmethod(5,26)
print(player3.name)
print(player3.age)