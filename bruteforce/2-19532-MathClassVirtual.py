a,b,c,d,e,f = map(int, input().split())

def check(x,y):
    return a*x+b*y == c and d*x+e*y == f

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if check(x,y):
            print(f'{x} {y}')
