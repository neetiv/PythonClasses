print('''Amazing Shipping Company

Catalog:
$3 Milk
$5 Chocolate Milk
$7 Eggs
$8 Bread
$10 Lettuce
$10 Potatoes
$15 Tomatoes
$15 Onions
$20 Raspberries
$20 Peaches
$20 Blackberries
$20 Strawberries

**all items are listed with the unit price
''')
grocery_list = []
amount = []
cost = []
more = 'y'
while more == 'y' or more == 'Y':
    hi = True
    what = input("What would you like to buy? (please write your answer the way it is written in the catalog):  ")
    while hi == True:
        if what == 'Milk':
            cost.append('3')
            hi = False
        elif what == 'Chocolate Milk':
            cost.append('5')
            hi = False
        elif what == 'Eggs':
            cost.append('7')
            hi = False
        elif what == 'Bread':
            cost.append('8')
            hi = False
        elif what == 'Lettuce' or what == 'Potatoes':
            cost.append('10')
            hi = False
        elif what == 'Tomatoes' or what == 'Onions':
            cost.append('15')
            hi = False
        elif what == 'Raspberries' or what == 'Peaches' or what == 'Strawberries' or what == 'Blackberries':
            cost.append('20')
            hi = False
        else:
            print("The value you have entered is invalid.")
            what = input("What would you like to buy? (please write your answer the way it is written in the catalog):  ")

    number = input("How many of the item would you like? (maximum 99):  ")
    error = number.isdecimal()
    while error == False or int(number)>=100:
        print("Please enter a valid number")
        number = input("How many of the item would you like?:  ")
        error = number.isdecimal()
    number = int(number)  
    grocery_list.append(what)
    amount.append(number)
    more = input('''Would you like to buy anything else?
    y = Yes
    n = No
    :  ''')
    




total = []

print('''
''')

for i in range(0, (int(len(grocery_list)))):
    x = int(14-((len(grocery_list[i]))))
    space = x * ' '
    y = int(len(str(amount[i])))
    if y == 1:
        spaces = 2*' '
    elif y == 2:
        spaces = ' '
    print(grocery_list[i], space, amount[i], spaces, '$', (int(cost[i]))*(int(amount[i])))
    total.append((int(cost[i]))*(int(amount[i])))
    
print("Total: $", sum(total))
