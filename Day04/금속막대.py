T = int(input())

for case in range(1, T+1):
    n = int(input())
    x = list(map(int, input().split()))
    f = x[0::2]
    b = x[1::2]
    a = 0
    l = []

    for i in range(n):
        if f[i] not in b:
            a = i
    
    for _ in range(n):
        l.append(str(f[a]))
        l.append(str(b[a]))
        for i in range(n):
            if b[a] == f[i]:
                a = i
                break
        
    print('#{} {}'.format(case, ' '.join(l)))
