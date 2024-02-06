N, M = map(int, input().split())

cards = list(map(int, input().split()))

s = 0
for i in range(len(cards)):
    for j in range(len(cards)):
        for k in range(len(cards)):
            if i == j or i == k or j == k:
                continue
            else:
                curr_sum = cards[i]+cards[j]+cards[k]
                if M-curr_sum >= 0 and M-curr_sum < M-s:
                    s = curr_sum

print(s)
