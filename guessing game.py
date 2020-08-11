import random
level = input('''
Level Selection:
1: Easy
2: Medium
3: Hard

''')

maximum = 0
guesses = 0
if level == '1':
    maximum = 100
    guesses = 8
elif level == '2':
    maximum = 1000
    guesses = 12
elif level == '3':
    maximum = 10000
    guesses = 30

num = random.randint(1, maximum)
guess = 0
percent = 0
while True:
    i = int(input('''
Guess a number between 1 and %s:  ''' % maximum))
    x = abs(num-i)
    percent = x/maximum

    if i == num:
        print('You guessed right!')
        break
    elif x <= 5:
        print("Very Hot")
    elif x <= 10:
        print("Hot")
    elif x <= 20:
        print("Warm")
    elif x <= 50:
        print("Cold")
    else:
        print("Very Cold")
        
    guess+=1
    if guess==guesses:
        print("You are out of guesses. The number was:  ", num)
        break
