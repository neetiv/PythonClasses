print('''Currency Conversion Calculator
''')
while True:
    convert = input('''
    Select a currency to convert US dollars into:
    A = Indian Rupees
    B = European Euros
    C = Japanese Yen
    D = Swiss Franc
    E = Russian Ruble
    F = Exit
    Type in the corresponding letter:  ''')
    if convert == 'F' or convert == 'f':
        print("You have successfully exited")
        break
    val = float(input("How many US dollars are you converting?:  "))
    if convert == 'A' or convert == 'a':
        print(val, "US dollars converted into Indian Rupees is", (val*75.55))
    elif convert == 'B' or convert == 'b':
        print(val, "US dollars converted into European Euros is", (val*0.89))
    elif convert == 'C' or convert == 'c':
        print(val, "US dollars converted into Japanese Yen is", (val*107.96))
    elif convert == 'D' or convert == 'd':
        print(val, "US dollars converted into Swiss Franc is", (val*0.95))
    elif convert == 'E' or convert == 'e':
        print(val, "US dollars converted into Russian Ruble is", (val*71.18))
