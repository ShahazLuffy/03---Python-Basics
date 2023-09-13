# object introspection is the ability to determine the type of an object at runtime
# because everything in python is an object it's one of the python's strength
class User(): #parent
    def __init__(self, email):
        self.email= email
    def signed_in(self):
        print('logged in')
    def attack(self):
        print('do nothing')
class Wizard(User): #child  (subclass / derived class)
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power
    def attack(self):   
        User.attack(self) 
        print(f'{self.name} attacking with power of  {self.power}') 
        
      
class Archer(User):#child  (subclass / derived class)
    def __init__(self, name, num_arrows,email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'{self.name} attacking with arrows : arrows-left {self.num_arrows}')

wizard1 = Wizard('Ali', 50, 'ali@gmail.com')
archer1 = Archer('Karim', 100, 'karim@gmail.com')

print(wizard1.email)
print(archer1.email) 

print(dir(wizard1)) # we have access to email, name, power, sign_in