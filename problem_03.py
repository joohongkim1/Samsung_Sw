# 숫자 카드

import copy

t = int(input())

for i in range(1, t+1):
    N = int(input())
    n = input()
    cnt = [0] * 10
    for j in range(0, N):
        cnt[int(n[j])] += 1
    temp = copy.deepcopy(cnt)
    for a in range(len(cnt)-1, 0, -1):
        for b in range(0, a):
            if cnt[b] > cnt[b+1]:
                cnt[b], cnt[b+1] = cnt[b+1], cnt[b]
    
    for c in range(9, -1, -1):
        if temp[c] == cnt[9]:            
            result = c
            break
    print('#%d %d %d' % (i, result, cnt[9]))
