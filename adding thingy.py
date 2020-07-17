num = str(input("Give a number(ex. a + aa + aaa... give a):  "))
val = int(input("Give the number of times that the first number will be repeated(ex. a + aa + aaa... give the maximum value that it will repeat): "))
lst = []
for i in range(0, val):
    s = (num*(val-i))
    lst.append(int(s))
print(sum(lst))
