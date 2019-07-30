# 구간합

t = int(input())


for case in range(1, t+1):
    val = []
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    
    for i in range(0, n-m+1):
        sum = 0
        for j in range(i, m+i):
            sum += x[j]
        val.append(sum)

    for i in range(len(val)-1, 0, -1):
        for j in range(0, i):
            if val[j] > val[j+1]:
                val[j], val[j+1] = val[j+1], val[j]
    diff = val[len(val)-1] - val[0]

    print('#%d %d' % (case, diff))
        