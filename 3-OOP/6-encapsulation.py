# encapsulation is binding data and functions that manipulate that data
# we encapsulate in one big object and we keep everything in that big box
# we call this data and functions >>> method and attributes
class PlayerCharacter: 
    def __init__(self, name, age): 
            self.name = name
            self.age = age
            
    def run(self):
        print('run')
    
    def speak(self):
        return f'my name is {self.name} and i am {self.age}'
        
player1 = PlayerCharacter('Tom' , 20)
print(player1.speak())

# this is encapsulation, if we had not PlayerCharacter class, we had bunch of attributes and functions
# with this class, we packed this functions and attributes

