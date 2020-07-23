num = int(input("Enter a number:  "))
store = num
factors = []

for g in range(2,(num)+1):
    while (int(num) % g == 0):
        factors.append(g)
        factors.append(' ')
        num = num/g
for x in range(1, len(factors)):
    if len(factors) % x != 0:
        factors[x] = 

print("The prime factorization of",store,"is",factors)
