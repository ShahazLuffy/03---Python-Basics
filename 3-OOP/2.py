class PlayerCharacter: # names are always singular
    def __init__(self, name, age): # a dunder method (magic method) we call it constructor method or init method
        self.name = name # attribute (property)
        self.age = age
    def run(self):
        print('self') 
        return 'done'    
    
player1 = PlayerCharacter('ali', 32)
player2 = PlayerCharacter('zahra', 33)
print(player1) 
print(player1.name) 
print(player1.age) 
print(player1.run()) 

player2.attack = 50
print(player2.attack)