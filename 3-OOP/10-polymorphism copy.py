# polymorephism = many forms
# different method name does different because different objects are calling them   

class User(): #parent
    def signed_in(self):
        print('logged in')
    def attack(self):
        print('do nothing')
        
        
class Wizard(User): #child  (subclass / derived class)
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):   
        User.attack(self) 
        print(f'{self.name} attacking with power of  {self.power}') 
        
      
class Archer(User):#child  (subclass / derived class)
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'{self.name} attacking with arrows : arrows-left {self.num_arrows}')

wizard1 = Wizard('Ali', 50)
archer1 = Archer('Karim', 100)

def player_attack(char):
    char.attack()

# see what is a polymorphism                  <<<<<<<<<<<<<<<<<<<<<<<<<<
# same function gives different output because of the differenct object we pass it into
player_attack(wizard1)
player_attack(archer1)

print('-------------------another example -----------------------------')
#another example
for char in [wizard1, archer1]:
    char.attack()
    
# even if we have attack method in User , we overwrited it in Wizard and Archer classes

# if we want to have User's attack method too, we can wrtie User.attack() in our subclasses or use super