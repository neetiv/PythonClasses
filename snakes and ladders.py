ladder_start = []
ladder_end = []
snake_start = []
snake_end = []
store = 0
ladder_num = 1
snake_num = 1
dice_roll = 0
position = 1

import random
for append_lists in range(0, 6):    
    ladder_start.append(random.randint(2, 99))
    ladder_end.append(random.randint(2, 99))
    snake_start.append(random.randint(2, 99))
    snake_end.append(random.randint(2, 99))
        
##print(ladder_start, ladder_end, snake_start, snake_end)

while True:
    limit = 100
    num = []
    for i in range(1, 11):
        num = []
        print('+----', 40*'-', '----+')
        if i%2 == 1:
            for x in range(0,10):
                num.append(limit)
                limit -= 1
        else:
            #print(limit)
            limit -= 9
            for x in range(0,10):
                num.append(limit)
                limit += 1
            limit -= 11
        first = num[0]
        second = num[1]
        third = num[2]
        fourth = num[3]
        fifth = num[4]
        sixth = num[5]
        seventh = num[6]
        eighth = num[7]
        ninth = num[8]
        tenth = num[9] 
        for e in range(0, 10):
            for t in range(0, 6):
                if ladder_start[t] == num[e]:
                    if e == 0:
                        first = 'LS'
                    elif e == 1:
                        second = 'LS'
                    elif e == 2:
                        third = 'LS'
                    elif e == 3:
                        fourth = 'LS'
                    elif e == 4:
                        fifth = 'LS'
                    elif e == 5:
                        sixth = 'LS'
                    elif e == 6:
                        seventh = 'LS'
                    elif e == 7:
                        eighth = 'LS'
                    elif e == 8:
                        ninth = 'LS'
                    elif e == 9:
                        tenth = 'LS'
                if ladder_end[t] == num[e]:
                    if e == 0:
                        first = 'LE'
                    elif e == 1:
                        second = 'LE'
                    elif e == 2:
                        third = 'LE'
                    elif e == 3:
                        fourth = 'LE'
                    elif e == 4:
                        fifth = 'LE'
                    elif e == 5:
                        sixth = 'LE'
                    elif e == 6:
                        seventh = 'LE'
                    elif e == 7:
                        eighth = 'LE'
                    elif e == 8:
                        ninth = 'LE'
                    elif e == 9:
                        tenth = 'LE'
                if snake_start[t] == num[e]:
                    if e == 0:
                        first = 'SS'
                    elif e == 1:
                        second = 'SS'
                    elif e == 2:
                        third = 'SS'
                    elif e == 3:
                        fourth = 'SS'
                    elif e == 4:
                        fifth = 'SS'
                    elif e == 5:
                        sixth = 'SS'
                    elif e == 6:
                        seventh = 'SS'
                    elif e == 7:
                        eighth = 'SS'
                    elif e == 8:
                        ninth = 'SS'
                    elif e == 9:
                        tenth = 'SS'
                if snake_end[t] == num[e]:
                    if e == 0:
                        first = 'SE'
                    elif e == 1:
                        second = 'SE'
                    elif e == 2:
                        third = 'SE'
                    elif e == 3:
                        fourth = 'SE'
                    elif e == 4:
                        fifth = 'SE'
                    elif e == 5:
                        sixth = 'SE'
                    elif e == 6:
                        seventh = 'SE'
                    elif e == 7:
                        eighth = 'SE'
                    elif e == 8:
                        ninth = 'SE'
                    elif e == 9:
                        tenth = 'SE'
            
        if num[0] == position:
            first = '•'
        elif num[1] == position:
            second = '•'
        elif num[2] == position:
            third = '•'
        elif num[3] == position:
            fourth = '•'
        elif num[4] == position:
            fifth = '•'
        elif num[5] == position:
            sixth = '•'
        elif num[6] == position:
            seventh = '•'
        elif num[7] == position:
            eighth = '•'
        elif num[8] == position:
            ninth = '•'
        elif num[9] == position:
            tenth = '•'
                
        print('|',first,'|',second,'|',third,'|',fourth,'|',fifth,'|',sixth,'|',seventh,'|',eighth,'|',ninth,'|',tenth,'|',)
        if i == 10:
            print('+----', 40*'-', '----+')

    dice_roll = random.randint(1,6)
    print("The number the dice rolled is", dice_roll)
    position += dice_roll


            
