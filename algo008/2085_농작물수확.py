import sys
sys.stdin = open("2085_input.txt")


TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    my_map = [list(map(int, input())) for _ in range(n)]

    ans = 0

    idx = n // 2
    for j in range(n):
        ans += my_map[idx][j]

    for i in range(1, n//2+1):
        for j in range(i, n-i):
            ans += my_map[idx-i][j]
            ans += my_map[idx+i][j]

    print('#{} {}'.format(tc, ans))


