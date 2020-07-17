num = int(input("Give a number:  "))
    
lst = []

for i in range(1, num+1): #factors
    if num % i == 0:
        lst.append(i)
print("The factors of",num,"are:",lst)



import math #perfect square
if len(lst) % 2 == 0:
   oddoreven = 'even'
else:
   oddoreven = 'odd'

if oddoreven == 'odd':
    print(num,"is a perfect square")
else:
    print(num,"is not a perfect square")


if num == 0: #prime/composite
        print(num,"is neither prime nor composite")
elif len(lst)==2:
    print(num,"is a prime number")
else:
    print(num,"is a composite number")
