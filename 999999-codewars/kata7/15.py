def validate_pin(pin):
    return True if int(pin)==0 and  len(str(pin))==4 or len(str(pin))==6 else False

print(validate_pin(0000))


print(len(str(0000))==4)

print(len("0000"))