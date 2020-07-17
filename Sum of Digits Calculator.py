print('''Sum of Digits Calculator

''')

num = int(input("Enter a Number: "))
ans = 0
og = num


while num > 0:
    rem = num % 10
    ans = ans + rem
    num = int(num/10)


print("The sum of all the digits of", og, "=", ans)
