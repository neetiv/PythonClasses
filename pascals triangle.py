r = int(input("How many rows do you want?:  "))
a = []


for i in range(0, r):
    n = 1
    if i == 0: #first
        a.append(n)
    elif i == 1: #second
        a.append(n) 
    else: #rest
        prev = a[0]
        for s in range(0, i):
            if s == 0:
                a.append(1)
            elif s == i:
                a.append(1)
                break
            else:
                c = prev + a[s]
                prev = a[s]
                a[s] = c
                

    print((r-i)*' ', a)
