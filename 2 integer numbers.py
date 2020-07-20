inp = input("Give two numbers(seperated by commas):  ")
nums = inp.split(',')
#print(nums)
lst = []
x = 0

for j in range(0, len(nums)):
    for i in range(1, int(nums[x])+1):
        if int(nums[x]) % i == 0:
            lst.append(i)
    print("The factors of",nums[x],"are:",lst)
    x = x+1
    lst.clear()

import math
gcd=(math.gcd(int(nums[0]),int(nums[1])))
print("The GCD of",nums[0],"and",nums[1],"is",gcd)

print("The LCM of",nums[0],"and",nums[1],"is",int((int(nums[0])*int(nums[1]))/gcd))
