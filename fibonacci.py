terms = int(input('''Enter the number of terms you want:
'''))

n1 = 0
n2 = 1

if terms < 1:
    print(''' Please enter a positive integer instead. ''')

elif terms == 1:
    print("Fibonacci sequence up to",terms,":")
    print(n1)

elif terms == 2:
    print("Fibonacci sequence up to",terms,":")
    print(n1)
    print(n2)

elif terms > 2:
    print("Fibonacci sequence up to",terms,":")
    print(n1)
    print(n2)
    for x in range(0, terms-2):
        ans = n1 + n2
        print(ans)
        n1 = n2
        n2 = ans
