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
    def check_arrow(self):
        print(f'{self.name} attacking with arrows : arrows-left {self.num_arrows}')
    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer): # multiple inheritance
    def __init__(self, name, power,arrow): 
        Archer.__init__(self, name,arrow) 
        Wizard.__init__(self, name,power) 
    
hybridborg1 =  HybridBorg('zari', 12,30)
hybridborg1.run()
hybridborg1.check_arrow()
hybridborg1.attack()
hybridborg1.signed_in()