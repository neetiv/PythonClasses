n1 = 0
n2 = 1
print(n1)
print(n2)
for x in range(0, 18):
    ans = n1 + n2
    print(ans)
    n1 = n2
    n2 = ans
