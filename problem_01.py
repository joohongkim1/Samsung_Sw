# min max

t = int(input())

for i in range(1, t+1):
    N = int(input())
    x = list(map(int, input().split()))
    for a in range(N-1, 0, -1):
        for b in range(0, a):
            if x[b] > x[b+1]:
                x[b], x[b+1] = x[b+1], x[b]
    print('#%d %d' % (i, x[-1] - x[0]))