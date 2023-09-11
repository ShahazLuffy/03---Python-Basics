class User(): #parent
    def signed_in(self):
        print('logged in')
class Wizard(User): #child  (subclass / derived class)
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):    
        print(f'{self.name} attacking with power of  {self.power}') 
        
class Archer(User):#child  (subclass / derived class)
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'{self.name} attacking with arrows : arrows-left {self.num_arrows}')

wizard1 = Wizard('Ali', 50)
archer1 = Archer('Karim', 100)
print(isinstance(wizard1, Wizard)) # True because wizard1 is an instance of Wizard Class
print(isinstance(wizard1, User)) # True because wizard1 is a subclass of User
print(isinstance(wizard1, object)) # True because everything in python is an object