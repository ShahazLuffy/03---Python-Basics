# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
def validate_pin(pin):
   a =  int(pin) and pin >0
   b = len(str(pin)) == 4 or len(str(pin)) == 6
   return True if a == True and b == True else False
print(validate_pin('a234'))