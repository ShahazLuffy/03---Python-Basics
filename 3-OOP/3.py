class PlayerCharacter: # names are always singular
    membership = True # class object attribute (it does not change for different instanciates)
    def __init__(self, name, age): # a dunder method (magic method) we call it constructor method or init method
        # self refers to PlayerCharacter
        if(self.membership):
            self.name = name # attribute (property) >> its dynamic
            self.age = age
    def shout(self): 
        print(f'my name is {self.name}') # we can use self here because we passed self as shout's parameter
        # if you don't write self.name I mean if you say  print(f'my name is {name}')
        # it will not work cause you did not mention self

    
player1 = PlayerCharacter('ali', 32)
player2 = PlayerCharacter('zahra', 33)

print(player2.name)
player2.attack = 50

print(player1.membership)
print(player2.membership)
player2.shout()
# print(PlayerCharacter.name) >>> error because name is not class object attribuet... 