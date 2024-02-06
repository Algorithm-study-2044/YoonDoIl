N = int(input())

def getDecompSum(n):
    s = n
    while n:
        s += (n % 10)
        n //= 10
    return s

from collections import defaultdict
d = defaultdict(list)
for i in range(N):
    d[getDecompSum(i)].append(i)

sums = d[N]
if sums:
    print(sums[0])
else:
    print(0)
