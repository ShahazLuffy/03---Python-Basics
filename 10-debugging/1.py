# the act of finding and removing bugs and errors from our code is called debugging
# linting = linting allows us to detect as we code some issues with our code
# num + 4  # this red line below the num+4 is built in linting
# IDE / Editors help us too for errors and formatting
# read error >> what the erros mean? for example "type errror"
# pdb = pytho debugger is a way to debuf our code, its built in module
import pdb

def add(n1, n2):
    pdb.set_trace()
    return  n1 + n2
print(add(13, 'akbar'))
"""
(Pdb) n1
13
(Pdb) n2
'akbar'
(Pdb) help 
(Pdb) clear
(Pdb) step
(Pdb) a # all argument
(Pdb) w
"""
help(pdb)