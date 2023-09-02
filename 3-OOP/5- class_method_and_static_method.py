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
      