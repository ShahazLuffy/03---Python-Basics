# private and public is related to abstraction
# we don't want anyone to modify run and introduce methods
# if we put _ underscore before our variables it means as a developer we should not change it
# there is no actual private variable in python
class PlayerCharacter: 
    def __init__(self, name, age, nationality): 
            self._name = name
            self._age = age
            self._nationality = nationality
            
    def run(self):
        print('run')
    
    def introduce(self):
        return f'my name is {self._name} and i am {self._age}'
    def nationaliy(self):   
        return self._nationality
        
player1 = PlayerCharacter('Tom' , 20, 'USA')
print(player1._name)
player1._name = 'reza'
print(player1._name)
