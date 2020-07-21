inp = input("Give two numbers(seperated by commas):  ")
nums = inp.split(',')
#print(nums)
one = []
two = []


for y in range(1, int(nums[0])):
    if int(nums[0]) % y == 0:
        one.append(y)
print("The factors of",nums[0],"are:",one)


for a in range(1, int(nums[1])):
    if int(nums[1]) % a == 0:
        two.append(a)
print("The factors of",nums[1],"are:",two)


##gcd = 1
##for i in range(0, len(one)):
##    for j in range(0, len(two)):
##        if one[-1*i] == two[-1*j]:
##            gcd=(one[-1*i])
##            print(gcd, "is the GCD of", nums[0], "and", nums[1])
##            break
##
####import math
####gcd=(math.gcd(int(nums[0]),int(nums[1])))
####print("The GCD of",nums[0],"and",nums[1],"is",gcd)
##
##print("The LCM of",nums[0],"and",nums[1],"is",int((int(nums[0])*int(nums[1]))/gcd))
