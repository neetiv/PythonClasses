inp = input("Give a list of numbers:  ")
a = inp.split(",")
ans = int(input("What should the sum of the numbers be?:  "))
ele = int(input("How many numbers in your list should make up that sum?:  "))
size = len(a)
g = []

    
for i in range(0, size-2):
    x = 0
    for t in range(0, ele):
        x = x+int(a[t+i])
 

    if x == ans:

        for y in range(0, ele):
            print(int(a[i+y]))
        g.append('x')
              

if len(g)==0:
    print("No numbers in your list qualify these requirements.")
    
