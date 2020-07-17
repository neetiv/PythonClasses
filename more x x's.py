val = 5
value = 0
spaces = val*' '
space = value*' '
difference = -2
x = 3
y = 1
for f in range(0, 5):
    if f == 2:
        print(4*' ', 'X')
    elif f == 3 or f == 4:
            print(x*' ', 'X', y*' ', 'X')
            x = x-2
            y = y*5

    else:
        print(space, 'X', spaces, 'X')
        spaces = (val + difference*2)*' '
        space = (value - difference)*' '
        if f < 2:
            difference = int(difference - 2)

        
