TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    a = list(map(int, input().split()))

    print('#%d' % tc, end=" ")
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    for i in range(len(a)):
        if i == 5:
            break
        print('{} {}'.format(a[len(a)-i-1], a[i]), end=" ")
    print()