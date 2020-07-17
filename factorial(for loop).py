val = input('''Enter a number:
''')

ans = 1

if int(val)<= 0:
    print(''' There are no negative factorials :(
Try a number greater than zero.''')
    
    
elif int(val)>= 1:
    for x in range (1, int(val)+1):
        ans = ans*x
    print("The factorial of ", val, " is : " , ans)
    


