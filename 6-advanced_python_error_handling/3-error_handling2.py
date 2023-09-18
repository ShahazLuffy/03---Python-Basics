# sometimes we really want to stop the program
# we use "raise value error"


while True:
    try:
        age = int(input('please enter you age '))
        print(age +1)
    except ZeroDivisionError:
        print('please inter a valid name')
        raise ZeroDivisionError('you cannot divide by zero')
    except:
        print('please inter aaaaaaa valid name')
        break
    else: # no exception
        print('thank you')
        break #because of this the can you hear me never will be reached
    finally: # runs at end of everything
        print('ok, I am finally done')
    print('can you hear me')
    
age = int(input('please enter you age '))

print(age + 1)