N = int(input())

mem = [-1] * (N+6)
mem[3] = 1
mem[5] = 1
for i in range(3,N+1):
    if mem[i] != -1:
        if mem[i+3] == -1 or mem[i]+1 < mem[i+3]:
            mem[i+3] = mem[i]+1
        if mem[i+5] == -1 or mem[i]+1 < mem[i+5]:
            mem[i+5] = mem[i]+1

print(mem[N])
