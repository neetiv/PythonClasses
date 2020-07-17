print('''Calculator
''')

import math

while True:
    # operation menu
    operation = input('''Choose an operation:
    1 = addition
    2 = subtraction
    3 = multiplication
    4 = division
    5 = square root
    6 = exponents
    7 = quit

    ''')
    # error management
    error = operation.isdecimal()
    while error == False or int(operation) > 7 or int(operation) < 1:
        print("The value you have entered is invalid. Please give a whole number value between 1 and 7.")
        operation = input('''Choose an operation:
        1 = addition
        2 = subtraction
        3 = multiplication
        4 = division
        5 = square root
        6 = exponents
        7 = exit

        ''')
        error = operation.isdecimal()
    operation = int(operation)     
    

    if operation == 7: # exiting and breaking the loop
        print("You have successfully exited.")
        break
    elif operation == 5: #square root
        one = input('Enter a number: ')
        error = one.isdecimal()
        while error == False: #error management
            print("The value you have entered is invalid")
            one = input('Enter a number: ')
            error = one.isdecimal()
        print('''
            ''')

        one = int(one) #converting to integer and math
        print('The answer is %s' % (math.sqrt(one)))
    elif operation == 6: # exponents
        one = input('Enter a number: ')
        while error == False: #error management
            print("The value you have entered is invalid")
            one = input('Enter a number: ')
            error = one.isdecimal()
        two = input('Enter the value of the exponent: ')
        while error == False:
            print("The value you have entered is invalid")
            two = input('Enter the value of the exponent: ')
            error = one.isdecimal()
        print('''
        ''')

        one = int(one) #math and converting to integers
        two = int(two)
        print('The answer is %s' % (one**two))    
        
        print('''

        ''')
    else:
        one = input('Enter a number: ') #entering values and error management
        error = one.isdecimal()
        while error == False:
            print("The value you have entered is invalid")
            one = input('Enter a number: ')
            error = one.isdecimal()
                
        print('''
        ''')
        two = input('Enter a second number: ')
        error = two.isdecimal()
        while error == False:
            print("The value you have entered is invalid")
            two = input('Enter a second number: ')
            error = two.isdecimal()
        
        
                
        print('''
        ''')
        
        
        if operation == 1: #math
            one = int(one)
            two = int(two)
            print('The answer is %s' % (one + two))
        elif operation == 2:
            one = int(one)
            two = int(two)
            print('The answer is %s' % (one - two))
        elif operation == 3:
            print('The answer is %s' % (one * two))
            one = int(one)
            two = int(two)
        elif operation == 4:
            if two == '0':
                print("The value you have entered is invalid")
                two = input('Enter a second number: ')
                error = two.isdecimal()
            else:
                one = int(one)
                two = int(two)
                print('The answer is %s' % (one/two))
        

        print('''

        ''')
        
