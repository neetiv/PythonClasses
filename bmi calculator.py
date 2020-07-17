print('''BMI Calculator:
''')
w = float(input("What is your weight?(pounds):  "))
w = w/2.205
print("What is your height?:  ")
f = float(input("Feet: "))
i = float(input("Inches: "))
h = (f+(i/12))*0.3048
print("Your BMI is", (w/(h**2)))
