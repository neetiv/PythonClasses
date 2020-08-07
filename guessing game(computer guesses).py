print('''Choose any integer between 1 and 100 and keep it in your mind. The computer will guess a number.
''')

small = 1
large = 100


while True:
    guess = int((small+large)/2)
    
    print("I guess", guess)
    ans = input('''
Tell the computer...
A: The number in your mind is higher
B: Your number in your mind is lower
C: The computer guessed right!
    
''')

    if ans == 'A' or ans == 'a':
        small = guess+1

    elif ans == 'B' or ans == 'b':
        large = guess-1

    elif ans == 'C' or ans == 'c':
        print("Your number was", guess, ":)")
        break
