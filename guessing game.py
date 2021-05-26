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
    guesses = 6
elif level == '2':
    maximum = 1000
    guesses = 7
elif level == '3':
    maximum = 10000
    guesses = 8

num = random.randint(1, maximum)
guess = 0
percent = 0
while True:
    i = int(input('''
Guess a number between 1 and %s:  ''' % maximum))
    percent = 100*((abs(num-i))/maximum)
    if i == num:
        print("You guessed correctly! :)")
        break
    elif level == '1':
        if i > num:
            print("Your number is higher than the computer's number")
        elif i < num:
            print("Your number is lower than the computer's number")
    else:
        print("You are", percent, "% away from the computer's number.")
        
        
    guess+=1
    if guess==guesses:
        print("You are out of guesses. The number was:  ", num)
        break
