class PlayerCharacter: 
    membership = True 
# we learned that we can have attribute for a class 
# but what about a method? we want method for class
    def __init__(self, name, age): 
        
        if(age > 18):
            self.name = name
            self.age = age
    def shout(self): 
        print(f'my name is {self.name}') 
      
    @classmethod
    def sum_numbers(num1,num2):
        return num1+num2

player1= PlayerCharacter('karim',22)
player1.sum_numbers(2)