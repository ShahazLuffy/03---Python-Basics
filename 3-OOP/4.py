class PlayerCharacter: 
    membership = True 
    def __init__(self, name, age): 
        
        if(age > 18):
            self.name = name
            self.age = age
    def shout(self): 
        print(f'my name is {self.name}') 
      
        

player1 = PlayerCharacter('reza', 32)
player2 = PlayerCharacter('zari', 12)
print(player1.name)
print(player2.name)
