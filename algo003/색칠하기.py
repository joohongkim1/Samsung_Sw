import sys
sys.stdin = open("색칠하기input.txt")


TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    my_map = [[0] * 10 for _ in range(10)]
    count = 0

    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                my_map[x][y] += color

    for i in range(10):
        for j in range(10):
            if my_map[i][j] == 3:
                count += 1

    print('#{} {}'.format(tc, count))