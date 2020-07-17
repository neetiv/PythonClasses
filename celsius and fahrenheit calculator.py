print('''Fahrenheit and Celsius Calculator
''')
while True:
    convert = input('''
    What would you like to convert?
    A) Fahrenheit to Celsius
    B) Celsius to Fahrenheit
    C) Exit
    Enter the corrresponding letter:''')
    if convert == 'C' or convert == 'c':
        print("You have successfully exited")
        break
    val = float(input("Please enter the value you would like to convert:   "))
    if convert == 'A' or convert == 'a':
        print(val, 'converted to Celsius equals ', ((val-32)*5/9))
    elif convert == 'B' or convert == 'b':
        print(val, 'converted to Fahrenheit equals ', ((val*9/5) + 32))
