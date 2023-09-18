def sum(num1, num2):
    try:
         return num1 + num2
     
    except TypeError as err:
        print(f'please enter a number ! + {err}')
        
    except (ValueError, ZeroDivisionError) as err:
        print(err)

print(sum('1', 2))