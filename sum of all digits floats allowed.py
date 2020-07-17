print('''Sum of Digits Calculator
''')

num = input("Enter a number(decimals OK):  ")


og = num
lst = []
counter = 0

for i in range(0, len(num)):
    if (num[i] != '.'):
        counter = counter+int(num[i])
print("The sum of all the digits of", og, "=", counter)
