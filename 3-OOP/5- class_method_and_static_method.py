class PlayerCharacter: 
    membership = True 
# we learned that we can have attribute for a class 
# but what about a method
    def __init__(self, name, age): 
        
        if(age > 18):
            self.name = name
            self.age = age
    def shout(self): 
        print(f'my name is {self.name}') 
    
    @classmethod  
    def addTwoNumbers(cls,num1, num2):   # cls  = PlayerCharacter 
        return num1+ num2
        # we can use cls to instanciate an object here
        #return cls('Tom', num1+ num2) # age = num1 + num2
        
    @staticmethod #same as class method except no cls
    def multiTwoNumbers(num1, num2):
        return num1* num2
    
    
    
     
player1 = PlayerCharacter('Tom' , 20)
print(player1.addTwoNumbers(1,3))
print(player1.multiTwoNumbers(4,5))

  
  
  
# it is a class method because we can use it without even instanciate it
print(PlayerCharacter.addTwoNumbers(3,5))