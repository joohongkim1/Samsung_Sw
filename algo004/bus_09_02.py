import sys
sys.stdin = open("bus_input.txt")


TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    bus_stop = [0] * 5001
    print('#{}'.format(tc), end=' ')
    for i in range(n):
        start, end = list(map(int, input().split()))
        for j in range(start, end+1):
            bus_stop[j] += 1
    p = int(input())
    for _ in range(p):
        c = int(input())
        print(bus_stop[c], end=" ")
    print()



