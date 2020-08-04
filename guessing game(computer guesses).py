print('''Choose any integer between 1 and 100 and keep it in your mind. The computer will guess a number.
''')
lst=[]
small = 0
large = 0

for i in range (1,101):
    lst.append(i)
#print(lst)

while True:
    print(len(lst))
    guess = lst[int(len(lst)/2)]
    
    print("I guess", guess)
    ans = input('''
Tell the computer...
A: Your number is higher
B: Your number is lower
C: The computer guessed right!
    
''')

    if ans == 'A' or ans == 'a':
        small = guess+1
        large = 

    elif ans == 'B' or ans == 'b':
        del lst[guess: lst[-2]]

    elif ans == 'C' or ans == 'c':
        print(":)")
        break

    
