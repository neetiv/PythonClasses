print("Calculator")

import math

while True:
    print('''
    ''')

    def add(one, two):
        return one+two
    def subtract(one, two):
        return one-two
    def multiply(one, two):
        return one*two
    def divide(one, two):
        return one/two
    def square_root(one):
        return math.sqrt(one)
    def powers(one, two):
        return one**two

    operation = input('''Choose an operation:
        1 = addition
        2 = subtraction
        3 = multiplication
        4 = division
        5 = square root
        6 = powers
        7 = quit

        ''')
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
    if operation == 7:
        print("You have successfully exited.")
        break
    elif operation == 5:

        number_1 = (input("Please enter a number:"))
        error = number_1.isdecimal()
        while error == False:
            print("The value you have entered is invalid.")
            number_1 = input('''Please enter a number:  ''')
            error = number_1.isdecimal()
        number_1 = int(number_1)

           
        print("The square root of", number_1, "=", square_root(number_1))
    elif operation == 6:

        number_1 = (input("Please enter a number:"))
        error = number_1.isdecimal()
        while error == False:
            print("The value you have entered is invalid.")
            number_1 = input('''Please enter a number:  ''')
            error = number_1.isdecimal()
        number_1 = int(number_1)

        number_2 = (input("Please enter the exponent value:  "))
        error = number_2.isdecimal()
        while error == False:
            print("The value you have entered is invalid.")
            number_1 = input('''Please enter the exponent value:  ''')
            error = number_1.isdecimal()
        number_2 = int(number_2)

            
        print(number_1, "to the power of", number_2, "=", powers(number_1, number_2))
    else:

        number_1 = (input("Please enter a number:"))
        error = number_1.isdecimal()
        while error == False:
            print("The value you have entered is invalid.")
            number_1 = input('''Please enter a number:  ''')
            error = number_1.isdecimal()
        number_1 = int(number_1)


        number_2 = (input("Please enter a second number:  "))
        error = number_2.isdecimal()
        while error == False:
            print("The value you have entered is invalid.")
            number_1 = input('''Please enter a second number:  ''')
            error = number_1.isdecimal()
        number_2 = int(number_2)
            
        
    if operation == 1: 
        print(number_1, "+", number_2, "=", add(number_1, number_2)) 
  
    elif operation == 2: 
        print(number_1, "-", number_2, "=", subtract(number_1, number_2)) 
      
    elif operation == 3: 
        print(number_1, "*", number_2, "=", multiply(number_1, number_2)) 
      
    elif operation == 4: 
        print(number_1, "/", number_2, "=", divide(number_1, number_2))
    
