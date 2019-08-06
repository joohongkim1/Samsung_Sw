T = int(input())

for case in range(1, T+1):
    n = int(input())
    aj = list(map(int, input().split()))

    for i in range(len(aj)-1, 0, -1):
        for j in range(0, i):
            if aj[j] > aj[j+1]:
                aj[j], aj[j+1] = aj[j+1], aj[j]
    
    print('#%d' % case, end=' ')
    for i in range(len(aj)-1, len(aj)-6, -1):
        print('%d %d' % (aj[i], aj[len(aj)-1-i]), end=' ')
    print()