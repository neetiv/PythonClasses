import random
num = random.randint(1, 100)
guess = 0
while True:
    i = int(input('''Guess a number between 1 and 100:  '''))
    if i == num:
        print('You guessed right!')
        guess+=1
        break
    elif i > num:
        print('Try lower')
        guess+=1
    elif i < num:
        print('Try higher')
        guess+=1
    if guess==6:
        print("You are out of guesses. The number was:  ", num)
        break
