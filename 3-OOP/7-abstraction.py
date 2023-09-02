# abstraction means hiding information or abstracting away the information and giving access to only what's necessary
# so whatever the user of the programmer or the machine is interested in, that's only thing we give access
# everything else , we kinda hide it in a blanked underneath the hood because they don't have to worry about it


class PlayerCharacter: 
    def __init__(self, name, age): 
            self.name = name
            self.age = age
            
    def run(self):
        print('run')
    
    def introduce(self):
        return f'my name is {self.name} and i am {self.age}'
        
player1 = PlayerCharacter('Tom' , 20)
print(player1.introduce())

# an example if abstraction, user do not konw and does not care how intrudce method is built