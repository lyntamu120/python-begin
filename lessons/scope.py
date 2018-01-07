my_name = 'ryu' #global variable

def print_name():
    global my_name # change the global name inside a function
    my_name = 'yoshi'
    print(f'the name inside the function is {my_name}')

print_name()
print(f'the name outside the function is {my_name}')
