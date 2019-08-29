import sys
sys.stdin = open("금속막대input.txt")

#
TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    stick = list(map(int, input().split()))
    even = []
    odd = []
    start = 0
    l = []
    print('#%d' % tc, end=' ')

    for i in range(0, len(stick), 2):
        even.append(stick[i])

    for i in range(1, len(stick), 2):
        odd.append(stick[i])

    for i in range(n):
        if even[i] not in odd:
            start = i

    for _ in range(n):
        l.append(even[start])
        l.append(odd[start])
        for i in range(n):
            if odd[start] == even[i]:
                start = i
                break

    for i in l:
        print(i, end=' ')
    print()


