num = int(input("Please Enter A Number:  "))

ans = 0
og = num
x = len(str(num))

while num > 0:
    rem = num % 10
    ans = ans + (rem**int(x))
    num = int(num/10)

if ans == og:
    print(og,"is an Armstrong Number")
else:
    print(og,"is not an Armstrong Number")


print('''
All Armstrong Numbers from 100 to 99999: ''')

for i in range(100,99999):
    store = i
    ans = 0
    x = len(str(i))
    while i > 0:
        rem = i % 10
        ans = ans + (rem**int(x))
        i = int(i//10)
    if ans == store:
        print(store)

