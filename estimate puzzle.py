def estimate(num, places):
    for i in range (1, places+1):
        num[(-1*i)] = 0
    print(*num)

num = []
inp = input("Give me a number (each integer should be seperated by spaces):  ")
num = inp.split(' ')
for j in range(len(num)):
    num[j] = int(num[j])
##print(num)
places = int(input("How many place values would you like to round?:  "))

estimate(num, places)
