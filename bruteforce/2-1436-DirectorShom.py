N = int(input())

def check(n):
    cnt = 0
    while n:
        if n%1000 == 666:
            return True
        n//=10

nth = 0
i = 0
while nth < N:
    if check(i):
        nth += 1
    i+=1

print(i-1)
