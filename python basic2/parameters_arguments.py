#parameter >> when we define function
def sayHello(name, family):
    print(f'hello {name} {family}')

#arguments >>Actual value when we call function
sayHello('ali', 'ghaderi pour')



#positional arguemnts
sayHello('ghaderi pour' , 'ali')


#keyword arguments
sayHello(family='ghaderi pour' , name='ali')

#default parameters
def say_hello(name, family='ghaderi pour'):
    print(f'hello {name} {family}')

say_hello('aliiiiiiiiiiii')